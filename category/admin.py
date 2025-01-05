from django.contrib import admin
from .models import Category

# Register your models here.
<<<<<<< HEAD

=======
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

<<<<<<< HEAD
admin.site.register(Category, CategoryAdmin)
=======
admin.site.register(Category, CategoryAdmin)
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
