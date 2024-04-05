from django.urls import path
from product import views as v
urlpatterns = [
    path('', v.index, name='index')
]