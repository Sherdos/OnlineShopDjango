from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from product.forms import LoginForm, RegisterForm, ReviewForm, UserCreationForm
from product.models import Review,  Product
from product.utils import search_product
from django.urls import reverse_lazy
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
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        Review.objects.create(text=form.data['text'],assesment=form.data['assesment'], user_id=form.data['user'], product_id = form.data['product'])
 
        return redirect('show_product', form.data['product'])
    
    


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
    

class UserRegisterView(generic.CreateView):
    template_name = 'pages/login.html'  
    form_class = RegisterForm
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return redirect('index')

def logout_user(request):
    logout(request)
    return redirect('index')

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'pages/login.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('index')