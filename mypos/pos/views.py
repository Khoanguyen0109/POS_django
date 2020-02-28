from django.shortcuts import render
import json

from .models import  Product, Customer, Bill, Item_in_bill,Shop ,Item_in_storage,Storage


#Return the main page
def dashboard(request):
    return render(request, 'dashboard.html')

#Login the shop and return product to make bill
def billing(request):
    if request.method == 'GET':
        return render(request, 'billing.html')
    else:
        sid = request.POST.get('shopID', None)
        listshop = Shop.objects.all()
        for i in listshop:
            if i.id_shop == sid:
                shop = Shop.objects.get(pk=sid)
                products = list(Product.objects.all())
                # context = { 'cust' : customer.identity,
                #             'name' : customer.name,
                #             'balance' : customer.balance,
                #             'products': products, }
                return render(request, 'billing_details.html', {'products': products, 'shop':shop})

        return render(request, 'billing.html')

#post bill to the DB and update quantity of products
def order(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        print(data)
        items = Item_in_storage.objects.all()
        stid= data['storage_id']
        storage = Storage.objects.get(pk=stid)
        order = Bill.objects.create(
                                    total_payment=data['total_price'],
                                    success=False)
        for product_id in data['product_ids']:
            Item_in_bill(product=Product.objects.get(pk=product_id), bill=order).save()
            for i in items:
                if i.storage.id_storage == data['storage_id'] and i.product.id_product == product_id :
                    if(i.quantity >0 ):
                        i.quantity=i.quantity-1
                        i.save()
                        order.success= True
                        storage.total= storage.total-1
                        storage.save() 
                    else:
                        order.success = False

        # if data['total_price'] <= customer.balance:
        #     customer.balance -= int(data['total_price'])
        #     customer.save()
        #     order.success = True
        order.save()
        return render(request, 'order.html', {'success' : order.success})




# def invoice_dashboard(request):
#     return render(request, 'invoice_dashboard.html')

# def customer_invoice(request):

#         customer_orders = Bill.objects.filter(success=True)
#         context = {'orders': [order for order in customer_orders],
#                 'total': sum([int(order.total_payment) for order in customer_orders]),
#                 }
#         return render(request, 'customer_invoice_detail.html', context)
 

# def get_bill_detail(request): 
    
#     if request.method ==" POST":
        
#         bid= request.POST.get(id_bill)
#     return render(request, 'bill_detail.html', )

