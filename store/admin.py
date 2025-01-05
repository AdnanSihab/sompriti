from django.contrib import admin
<<<<<<< HEAD
from .models import Product, Variation, ReviewRating, ProductGallery
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
=======
from .models import Product, Variation

# Register your models here.
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
<<<<<<< HEAD
    inlines = [ProductGalleryInline]
=======
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

admin.site.register(Product, ProductAdmin)
<<<<<<< HEAD
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
=======
admin.site.register(Variation, VariationAdmin)
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
