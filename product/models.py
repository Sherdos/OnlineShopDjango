from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
choices_review = (
 ('1','1'),
 ('2','2'),
 ('3','3'),
 ('4','4'),
 ('5','5'),
 ('6','6'),
 ('7','7'),
 ('8','8'),
 ('9','9'),
 ('10','10'),
)

class Product(models.Model):
    """Model definition for Product."""
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='опесание')
    price = models.PositiveIntegerField(verbose_name='цена')
    categories = models.ManyToManyField('product.Category', verbose_name='категории')
    # TODO: Define fields here
    sizes =models.ManyToManyField('product.Size', verbose_name='размеры')
    rating = models.IntegerField(verbose_name='рейтинг', default=0)
    
    
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
    

class Review(models.Model):
    """Model definition for Review."""
    text = models.TextField(verbose_name='Отзыв')
    assesment = models.CharField(verbose_name='Оценка', max_length=50, choices=choices_review)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='продукт')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    created = models.DateTimeField(verbose_name='дата', auto_now_add=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Review."""

        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        """Unicode representation of Review."""
        return f'{self.user}'


