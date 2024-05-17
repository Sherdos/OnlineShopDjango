from django.urls import path
from product import views as v



urlpatterns = [
    path('', v.IndexView.as_view(), name='index'),
    path('products/', v.ProductsView.as_view(), name='products'),
    path('product/show/<int:pk>', v.ShowProductView.as_view(), name='show_product'),
    path('product/add/review/', v.AddReviewView.as_view(), name='add_review'),
    path('product/search/', v.SearchProductView.as_view(), name='search'),
    path('product/add/cart/', v.AddCartView.as_view(), name='add_cart'),
    
    
]