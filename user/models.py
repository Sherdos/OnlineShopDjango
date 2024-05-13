from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class Profie(models.Model):
    """Model definition for Profile."""
    user = models.ForeignKey('user.User',on_delete=models.CASCADE, related_name='user_pro')
    text = models.TextField(verbose_name='about me', default='Я эдесь')
    phone = models.IntegerField(verbose_name='phone number', null=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user}'
    

class User(AbstractUser):
    
    
    def save(self, *agr, **kwarg) -> None:
        user = super().save(*agr,**kwarg)
        Profie.objects.get_or_create(user_id=self.pk)
        return user
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})
    

class Cart(models.Model):
    """Model definition for Cart."""
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='Пользователь', related_name='cart_user')

    # TODO: Define fields here
    def get_absolute_url(self):
        return reverse('cart', kwargs={'pk': self.pk})
    class Meta:
        """Meta definition for Cart."""

        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        
class CartProduct(models.Model):
    card = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='Карта', related_name='cart_product')
    count = models.PositiveIntegerField(verbose_name='количество')
    cart = models.ForeignKey('user.Cart', on_delete=models.CASCADE, verbose_name='Корзина', related_name='cart_card')

    
    def __str__(self):
        return f'{self.card.title}'

    