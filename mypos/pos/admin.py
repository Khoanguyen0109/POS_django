from django.contrib import admin
from .models import Product,Bill,Item_in_bill,Shop,Storage,Item_in_storage, ExportStorage,Item_export, ImportStorage,Item_import


admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Item_in_bill)
admin.site.register(Shop)
admin.site.register(Storage)
admin.site.register(Item_in_storage)
admin.site.register(ExportStorage)
admin.site.register(Item_export)
admin.site.register(ImportStorage)
admin.site.register(Item_import)
# Register your models here.
