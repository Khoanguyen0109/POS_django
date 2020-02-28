from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.exporting, name='exporting'),
    # path('/exportlist', views.order, name='exportlist'),
    path('export', views.export, name='export'),
    
]