from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
<<<<<<< HEAD
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
=======
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
<<<<<<< HEAD
    return dict(cart_count=cart_count)
=======
    return dict(cart_count=cart_count)
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
