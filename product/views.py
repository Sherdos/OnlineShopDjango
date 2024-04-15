from django.shortcuts import render

from product.forms import Review
from product.models import Product
from product.utils import search_product
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
    if request.method == 'POST':
        form = Review(request.POST)
        if form.is_valid():
            review_num = int(form.data['review'])
            card.rating += review_num
            
    form_review = Review()
    context = {
        'title':f'{card.title}',
        'card':card,
        'form_review':form_review
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

def search(request):
    template_name = 'pages/clothes.html'
    cards = search_product(request)
    context = {
        'title':"Одежда",
        'cards':cards        
    }
    return render(request, template_name ,context)