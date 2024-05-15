from django.contrib import admin
from user.models import User, Profie, Cart, CartProduct
# Register your models here.

admin.site.register(User)
admin.site.register(Profie)
admin.site.register(Cart)
admin.site.register(CartProduct)