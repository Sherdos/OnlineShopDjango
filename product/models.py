from django.db import models

# Create your models here.

class Product(models.Model):
    """Model definition for Product."""
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='опесание')
    price = models.PositiveIntegerField(verbose_name='цена')
    image = models.ImageField(verbose_name='фото', upload_to='image/product/')
    # TODO: Define fields here

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title}'
