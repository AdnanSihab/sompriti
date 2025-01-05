from django.db import models
from store.models import Product, Variation
<<<<<<< HEAD
from accounts.models import Account
=======
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b


# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
<<<<<<< HEAD
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
=======
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
<<<<<<< HEAD
=======
    # def __str__(self):
    #     # Return a string that includes the product name, variations, and quantity
    #     variation_names = ', '.join([str(variation) for variation in self.variations.all()])
    #     variation_part = f" ({variation_names})" if variation_names else ""
    #     return f"{self.product.product_name}{variation_part} - {self.quantity} pcs"
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
