from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('billing/', views.billing, name='billing'),
    path('billing/order', views.order, name='order'),
    # path('invoiceggg', views.invoice_dashboard, name='invoice_dashboard'),
    # path('invice/customer/', views.customer_invoice, name='customer_invoice')
    
]
