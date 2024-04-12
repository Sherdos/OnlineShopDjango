from django.shortcuts import render

from product.models import Product

# Create your views here.

def index(request):
    template_name = 'pages/index.html'
    cards = Product.objects.all().order_by('id').reverse()[:3]
    context = {
        'title':"Главная",
        'cards':cards        
    }
    return render(request, template_name,context)

def show_product(request, pk):
    template_name = 'pages/show_product.html'
    card = Product.objects.get(id=pk)
    context = {
        'title':f'{card.title}',
        'card':card
    }
    return render(request, template_name,context)

def products(request):
    template_name = 'pages/clothes.html'
    cards = Product.objects.all()
    context = {
        'title':"Одежда",
        'cards':cards        
    }
    return render(request, template_name,context)
