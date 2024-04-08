from django.contrib import admin
from product import models
# Register your models here.
class MediaInline(admin.StackedInline):
    model = models.ProductMedia
    extra = 1

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    inlines = [
        MediaInline
    ]
    