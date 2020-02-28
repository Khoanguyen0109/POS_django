from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.importing, name='importing'),
    path('import', views.import_, name='import_'),
    
]