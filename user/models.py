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

        verbose_name = 'Profilee'
        verbose_name_plural = 'Profilees'

    def __str__(self):
        return f'{self.user}'
    

class User(AbstractUser):
    
    
    def save(self, *agr, **kwarg) -> None:
        user = super().save(*agr,**kwarg)
        Profie.objects.get_or_create(user_id=self.pk)
        return user
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})
    
    