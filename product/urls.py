from django.urls import path
from product import views as v
urlpatterns = [
    path('', v.IndexView.as_view(), name='index'),
    path('products/', v.ProductsView.as_view(), name='products'),
    path('product/show/<int:pk>', v.ShowProductView.as_view(), name='show_product'),
    path('product/search/', v.SearchProductView.as_view(), name='search'),
    path('login/', v.login_user, name='login'),
    path('register/', v.UserRegister.as_view(), name='register'),
    path('logout/', v.logout_user, name='logout'),
]