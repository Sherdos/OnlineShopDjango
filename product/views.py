from django.shortcuts import render

from product.models import Product

# Create your views here.

def index(request):
    template_name = 'pages/index.html'
    cards = Product.objects.all()
    context = {
        'title':"Главная",
        'cards':cards        
    }
    return render(request, template_name,context)

def show_product(request, id):
    template_name = 'pages/show_product.html'
    card = Product.objects.get(id=id)
    context = {
        'title':f'{card.title}',
        'card':card
    }
    return render(request, template_name,context)

