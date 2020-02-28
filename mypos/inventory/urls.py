from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_check, name='inventory'),
    
] 