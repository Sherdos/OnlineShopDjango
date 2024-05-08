from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from product.forms import  ReviewForm
from product.models import Review,  Product
from product.utils import search_product
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'cards'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        cards = Product.objects.all()[:3]
        return cards

class ShowProductView(generic.DetailView, generic.CreateView):
    model = Product
    template_name = 'pages/show_product.html'
    context_object_name = 'card'
    form_class = ReviewForm
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_review'] = ReviewForm()
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
            review = form.save(commit=False)
            review.user_id = form.data['user']
            review.product_id = form.data['product']
            review.save()
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
    
