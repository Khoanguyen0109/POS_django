
from django.shortcuts import render
import json

from pos.models import  Product, ExportStorage,Item_export ,Item_in_storage,Storage
# Create your views here.
def exporting(request):
    if request.method == 'GET':
        return render(request, 'export.html')
    else:
        stid = request.POST.get('storageID', None)
        liststorage = Storage.objects.all()
        for i in liststorage:
            if i.id_storage == stid:
                storage = Storage.objects.get(pk=stid)
                products = list(Product.objects.all())
                # context = { 'cust' : customer.identity,
                #             'name' : customer.name,
                #             'balance' : customer.balance,
                #             'products': products, }
                return render(request, 'export_list.html', {'products': products, 'storage':storage})

        return render(request,'export.html')

def export(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        print(data)
        items = Item_in_storage.objects.all()
        storages = Storage.objects.all()
        stid= data['storage_id']
        storage = Storage.objects.get(pk=stid)
        namelist= data['namelist']

        exportlist = ExportStorage.objects.create(      name_of_export_list= namelist,
                                                        storage_export= storage ,
                                                        total_export=data['total'],
                                                        success=False)  
        for product_id in data['product_ids']:
           
            for i in items:
                if i.storage.id_storage == stid and i.product.id_product == product_id :
                    
                    if(i.quantity >0 ):
                        Item_export(product=Product.objects.get(pk=product_id),exportStorage =exportlist).save()
                        
                        i.quantity=i.quantity-1
                        i.save()
                        storage.total= storage.total-1
                        storage.save()  
                        exportlist.success= True
                    else:
                        exportlist.success = False

        # if data['total_price'] <= customer.balance:
        #     customer.balance -= int(data['total_price'])
        #     customer.save()
        #     order.success = True
        exportlist.save()
        return render(request, 'order_export.html', {'success' : exportlist.success})
