from django.db import models

# Create your models here.

class Product(models.Model):
    """Model definition for Product."""
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='опесание')
    price = models.PositiveIntegerField(verbose_name='цена')
    # TODO: Define fields here

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

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
