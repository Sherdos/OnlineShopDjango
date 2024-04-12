from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    """Model definition for Product."""
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='опесание')
    price = models.PositiveIntegerField(verbose_name='цена')
    categories = models.ManyToManyField('product.Category', verbose_name='категории')
    # TODO: Define fields here
    sizes =models.ManyToManyField('product.Size', verbose_name='размеры')
    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('show_product', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f'{self.title}'


class ProductMedia(models.Model):
    """Model definition for ProductMedia."""

    # TODO: Define fields here

    image = models.ImageField(verbose_name='фото', upload_to='image/product/')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='product_media')
    
    
    
    class Meta:
        """Meta definition for ProductMedia."""

        verbose_name = 'Медиа Продукта'
        verbose_name_plural = 'Медии Продуктов'

    def __str__(self):
        return f'{self.product.title}'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    slug = models.SlugField(max_length=255, verbose_name='слаг')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return f'{self.title}' # TODO
    
class Size(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    slug = models.SlugField(max_length=255, verbose_name='слаг')
    
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
    
    def __str__(self):
        return f'{self.title}' # TODO
    
