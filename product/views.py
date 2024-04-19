from django.shortcuts import redirect, render

from product.forms import Review
from product.models import Product
from product.utils import search_product
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views import generic

# Create your views here.

# def index(request):
#     template_name = 'pages/index.html'
#     cards = Product.objects.all().order_by('id').reverse()[:3]
#     context = {
#         'title':"Главная",
#         'cards':cards
#     }
#     return render(request, template_name,context)

class IndexView(generic.ListView):
    model = Product
    template_name = 'pages/index.html'
    context_object_name = 'cards'


# def show_product(request, pk):
#     template_name = 'pages/show_product.html'
#     card = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         form = Review(request.POST)
#         if form.is_valid():
#             review_num = int(form.data['review'])
#             card.rating += review_num

class ShowProductView(generic.DetailView, generic.CreateView):
    model = Product
    template_name = 'pages/show_product.html'
    context_object_name = 'card'
    form_class = Review


def products(request):
    template_name = 'pages/clothes.html'
    cards = Product.objects.all()
    context = {
        'title':"Одежда",
        'cards':cards        
    }
    return render(request, template_name,context)

def search(request):
    template_name = 'pages/clothes.html'
    cards = search_product(request)
    context = {
        'title':"Одежда",
        'cards':cards        
    }
    return render(request, template_name ,context)

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