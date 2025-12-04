from .models import Category, CartItem

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def cart_item_count(request):
    if request.user.is_authenticated:
        return {
            'cart_item_count': CartItem.objects.filter(user=request.user).count()
        }
    return {
        'cart_item_count': 0
    }
