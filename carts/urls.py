from django.urls import path
from . import views

<<<<<<< HEAD

=======
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
<<<<<<< HEAD

    path('checkout/', views.checkout, name='checkout'),
]
=======
]
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
