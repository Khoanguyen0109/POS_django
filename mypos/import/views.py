from django.shortcuts import render
import json
# Create your views here.
from pos.models import  Product, ImportStorage,Item_import ,Item_in_storage,Storage
# Create your views here.
def importing(request):
    if request.method == 'GET':
        return render(request, 'import.html')
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
                return render(request, 'import_list.html', {'products': products, 'storage':storage})

        return render(request,'import.html')
def import_(request):
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
        products = Product.objects.all()

        importlist = ImportStorage.objects.create(      name_of_import_list= namelist,
                                                        storage_import= storage ,
                                                        total_import=data['total'],
                                                        success=False)
        for product_id in data['product_ids']:
            if check_exist(product_id)== True and check_in_storage(product_id) == False:
                Item_in_storage(product=Product.objects.get(pk=product_id),storage =storage,quantity=0).save()



        for product_id in data['product_ids']:
            Item_import(product=Product.objects.get(pk=product_id),importStorage =importlist).save()
            for i in items:
                if i.storage.id_storage == stid and i.product.id_product == product_id :
                    i.quantity=i.quantity+1
                    i.save()
                    storage.total= storage.total + 1
                    storage.save()
                    importlist.success= True

                    

        # if data['total_price'] <= customer.balance:
        #     customer.balance -= int(data['total_price'])
        #     customer.save()
        #     order.success = True
        importlist.save()
        return render(request, 'order2.html', {'success' : importlist.success})

def check_in_storage(id):
    items = Item_in_storage.objects.all()
    for i in items:
        if id == i.product.id_product:
            return True
    return False

def check_exist (id):
    products = Product.objects.all ()
    for i in products:
        if id == i.id_product:
            return True
    return False