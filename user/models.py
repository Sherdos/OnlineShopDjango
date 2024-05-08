from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profie(models.Model):
    """Model definition for Profile."""
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_pro')
    text = models.TextField(verbose_name='about me', default='Я эдесь')
    phone = models.IntegerField(verbose_name='phone number', null=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profilee'
        verbose_name_plural = 'Profilees'

    def __str__(self):
        """Unicode representation of Profilee."""
        pass
