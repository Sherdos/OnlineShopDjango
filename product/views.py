from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from product.forms import  CartProductForm, ReviewForm
from product.models import Review,  Product
from product.utils import search_product
from django.views import generic

from user.models import CartProduct

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'cards'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-rating')[:3]
        return cards

class AddCartView(generic.CreateView):
    model = CartProduct
    form_class = CartProductForm
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            order = form.save(commit=False)
            order.card_id = form.data['card_id']
            order.cart_id = form.data['cart_id']
            order.save()
            return redirect('show_product', form.data['card_id'])
        HttpResponse('Неправильный запрос', status=400)

class ShowProductView(generic.DetailView, generic.CreateView):
    model = Product
    template_name = 'pages/show_product.html'
    context_object_name = 'card'
    form_class = ReviewForm
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_cart'] = CartProductForm()
        title = context['card'].title
        context['title'] = f'{title}'
        context['cards'] = self.get_same_card(context['card'].categories.first())
        return context
    
    def get_same_card(self, cat):
        cards = Product.objects.filter(categories=cat.id)
        return cards
        
    
class AddReviewView(generic.CreateView):
    template_name = 'pages/show_product.html'
    form_class = ReviewForm
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            prduct = Product.objects.get(id=form.data['product'])
            new_rating = (prduct.rating * len(prduct.review_product.all())) + int(form.cleaned_data['assesment'])
            review = form.save(commit=False)
            review.user_id = form.data['user']
            review.product = prduct
            review.save()
            prduct.rating = new_rating / len(prduct.review_product.all())
            prduct.save()
            return redirect('show_product', form.data['product'])
        
        return HttpResponse('Неправильный запрос', status=400)
    


class ProductsView(generic.ListView):
    paginate_by = 2
    template_name = 'pages/clothes.html'
    context_object_name = 'cards'
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all().order_by('-id')
        return cards


class SearchProductView(generic.ListView):
    template_name = 'pages/clothes.html'
    context_object_name = 'cards'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск'
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        cards = search_product(self.request)
        return cards
    
