from django import template
from product.models import Product


register = template.Library()

@register.simple_tag()
def get_new_products():
    cards = Product.objects.all().order_by('-id')[:3]
    return cards
    
@register.inclusion_tag('tag/stars.html')
def get_rate_stars(rating):
    return {'stars':range(int(rating)//2), 'float':int(rating)%2}


@register.filter()
def avg_review(value):
    
    review_assesment = []
    for i in value:
        review_assesment.append(int(i.assesment))
    try:
        return sum(review_assesment) / len(review_assesment)
    except ZeroDivisionError:
        return 0
    


