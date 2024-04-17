from django.urls import path
from product import views as v
urlpatterns = [
    path('', v.index, name='index'),
    path('products/', v.products, name='products'),
    path('product/show/<int:pk>', v.show_product, name='show_product'),
    path('product/search/', v.search, name='search'),
    path('login/', v.login_user, name='login'),
    path('register/', v.register_user, name='register'),
    path('logout/', v.logout_user, name='logout'),
]