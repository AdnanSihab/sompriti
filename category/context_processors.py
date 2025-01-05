from .models import Category

def menu_links(request):
    links = Category.objects.all()
<<<<<<< HEAD
    return dict(links=links)
=======
    return dict(links=links)
>>>>>>> a1a51b03e61ddd11f3321dc643d2ca2a3ab46f5b
