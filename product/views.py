from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from product.forms import RegisterForm, ReviewForm, UserCreationForm
from product.models import Review,  Product
from product.utils import search_product
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'cards'
    
    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-id')[:3]
        return cards

class ShowProductView(generic.DetailView, generic.CreateView):
    model = Product
    template_name = 'pages/show_product.html'
    context_object_name = 'card'
    form_class = ReviewForm
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_review'] = ReviewForm()
        return context
    
class AddReviewView(generic.CreateView):
    template_name = 'pages/show_product.html'
    form_class = ReviewForm
    
    


class ProductsView(generic.ListView):
    template_name = 'pages/clothes.html'
    context_object_name = 'cards'
    
    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-id')
        return cards


class SearchProductView(generic.ListView):
    template_name = 'pages/clothes.html'
    context_object_name = 'cards'
    
    def get_queryset(self) -> QuerySet[Any]:
        cards = search_product(self.request)
        return cards
    
    


def login_user(request):
    template_name = 'pages/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('index')
    context = {
        'title':"Войти в Аккаунт",  
    }
    return render(request, template_name ,context)

class UserRegister(generic.CreateView):
    template_name = 'pages/login.html'  
    form_class = RegisterForm
    

def register_user(request):
    template_name = 'pages/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return redirect('index')
    context = {
        'title':"Заригистрироваться в Аккаунт",  
    }
    return render(request, template_name ,context)

def logout_user(request):
    logout(request)
    return redirect('index')