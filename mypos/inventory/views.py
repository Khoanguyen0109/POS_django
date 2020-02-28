from django.shortcuts import render
from pos.models import  Product,Storage,Item_in_storage

# Check storage
def inventory_check(request):
    if request.method == 'GET':
        return render(request, 'inventory.html')
    else:
        stid = request.POST.get('storageID', None)
        listitem = Item_in_storage.objects.all()
        storages = Storage.objects.all()
        mylist = []
        for st in storages:
            if st.id_storage == stid:
                storage = Storage.objects.get(pk=stid)
                for item in listitem:
                    if item.storage.id_storage == storage.id_storage:
                        mylist.append(item)
                    
                

                return render(request, 'storage.html', {'mylist': mylist, 'storage':storage})

        return render(request, 'inventory.html')