from django.urls import path
from user import views as v
urlpatterns = [
    path('login/', v.UserLoginView.as_view(), name='login'),
    path('register/', v.UserRegisterView.as_view(), name='register'),
    path('logout/', v.logout_user, name='logout'),
    path('profile/<int:pk>', v.Profile.as_view(), name='profile'),
]