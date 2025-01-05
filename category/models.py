from django.db import models
from django.urls import reverse

# Create your models here.
<<<<<<< HEAD

=======
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('products_by_category', args=[self.slug])

    def __str__(self):
<<<<<<< HEAD
        return self.category_name
=======
        return self.category_name
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
