from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Shop(models.Model):
    id_shop = models.CharField(max_length=5,primary_key=True)
    name_shop = models.CharField(max_length=120)

    
class Customer(models.Model):
    name_customer=models.CharField(max_length=120)
    SDT=models.CharField(max_length=11)

class Product (models.Model):
    CATEGORY =[
        ('Footwear','footwear'),
        ('Apparel','apparel'),
        ('Accessories','accessories')
    ]

    id_product = models.IntegerField(primary_key= True)
    name_product = models.CharField(max_length=150)
    size = models.CharField(max_length =5)
    Category = models.TextField(choices=CATEGORY)
    price = models.FloatField()
    
    def __str__(self):              
        return 'Name: {0}  Size: {1} '.format(self.name_product, self.size)

class Bill(models.Model):
    published_date = models.DateTimeField(auto_now=True)
    # shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    #product = models.ManyToManyField(Product,through='Item_in_bill')
    total_payment= models.FloatField()
    success = models.BooleanField(default=False)
    def __str__(self):              
        return 'ID: {0}  '.format(self.id)

class Item_in_bill(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    # quantity = models.IntegerField()
    # discount = models.FloatField()
    # price_after_discount= models.FloatField()
    def __str__(self):              
        return 'Id Bill: {0}  Product: {1}  Size: {2}'.format(self.bill.id, self.product.name_product, self.product.size)
    
class Storage (models.Model):
    id_storage = models.CharField(max_length=10,primary_key=True)
    name_storage = models.CharField(max_length=20)
    # product_in_storage =models.ManyToManyField(Product,through='Item_in_storage')
    total= models.IntegerField()
    def __str__(self):              
        return self.name_storage

class Item_in_storage(models.Model):
    storage=models.ForeignKey(Storage,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity= models.IntegerField()
    def __str__(self):              
        return 'Storage: {0}  Product: {1}  Size: {2}'.format(self.storage.id_storage, self.product.name_product, self.product.size)

class ExportStorage (models.Model):
    name_of_export_list= models.CharField(max_length=150)
    export_date = models.DateTimeField(blank=True, null=True)
    storage_export = models.ForeignKey(Storage,on_delete=models.CASCADE)
    # product_export =models.ManyToManyField(Product,through='Item_export')
    total_export= models.IntegerField()
    success = models.BooleanField(default=False)
    def publish(self):
        self.export_date = timezone.now()
        self.save()
    def __str__(self):              
        return 'Export Storage: {0}  Name of list : {1}  '.format(self.storage_export.id_storage, self.name_of_export_list)


class Item_export (models.Model):
    exportStorage =models.ForeignKey(ExportStorage,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    # quantity= models.IntegerField()
    def __str__(self):              
        return 'Export List: {0}  Product: {1}  Size: {2}'.format(self.exportStorage.name_of_export_list, self.product.name_product, self.product.size)

class ImportStorage (models.Model):
    name_of_import_list= models.CharField(max_length=150)
    import_date = models.DateTimeField(blank=True, null=True)
    storage_import = models.ForeignKey(Storage,on_delete=models.CASCADE)
    # product_inmport =models.ManyToManyField(Product,through='Item_import')
    success = models.BooleanField(default=False)    
    total_import= models.IntegerField()
    def publish(self):
        self.import_date = timezone.now()
        self.save()
    def __str__(self):              
        return 'Import Storage: {0}  Name of list : {1}  '.format(self.storage_import.id_storage, self.name_of_import_list)



class Item_import(models.Model):
    importStorage=models.ForeignKey(ImportStorage,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    # quantity= models.IntegerField()
    def __str__(self):              
        return 'Import List: {0}  Product: {1}  Size: {2}'.format(self.importStorage.name_of_import_list, self.product.name_product, self.product.size)