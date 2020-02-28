from django import forms 
from .models import Bill,Item_in_bill

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id_product', 'name_product', 'size', 'Category', 'price')