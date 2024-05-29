from django.urls import path
from user import views as v
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('login/', v.UserLoginView.as_view(), name='login'),
    path('register/', v.UserRegisterView.as_view(), name='register'),
    path('logout/', v.logout_user, name='logout'),
    path('profile/<int:pk>',  (v.Profile.as_view()), name='profile'),
    path('cart/<int:pk>', v.CartDetailView.as_view(), name='cart'),
]