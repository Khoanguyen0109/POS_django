from django.shortcuts import render
from pos.models import Product, Customer, Bill, Item_in_bill

def invoice_dashboard(request):
    return render(request, 'invoice_dashboard.html')

def customer_invoice(request):
    
        customer_orders = Bill.objects.filter(success=True)
        context = {'orders': [order for order in customer_orders],
                'total': sum([int(order.total_payment) for order in customer_orders]),
                }
        return render(request, 'customer_invoice_detail2.html', context)
 
def detail(request):
        items = Product.objects.all()
        
        return render(request, 'detail.html',{'items': items})