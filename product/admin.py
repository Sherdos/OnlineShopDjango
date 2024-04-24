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
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}

@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    '''Admin View for Category'''
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    '''Admin View for Review'''
    list_display = ('user',)