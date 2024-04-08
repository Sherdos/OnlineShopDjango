from django.urls import path
from product import views as v
urlpatterns = [
    path('', v.index, name='index'),
    path('product/show/<int:id>/', v.show_product, name='show_product'),
    
]