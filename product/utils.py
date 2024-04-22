

from product.models import Product



def search_product(request):
    key = request.GET.get('key')
    cards = Product.objects.filter(title__icontains=key)
    return cards