from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')

admin.site.register(Cart, CartAdmin)
<<<<<<< HEAD
admin.site.register(CartItem, CartItemAdmin)
=======
admin.site.register(CartItem, CartItemAdmin)
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
