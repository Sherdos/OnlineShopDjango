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

