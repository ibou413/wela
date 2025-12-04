from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, CartItem
from django.http import HttpResponse
from .forms import ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test

def fix_slugs(request):
    """
    A temporary view to programmatically fix categories with empty slugs.
    """
    count = 0
    for category in Category.objects.filter(slug__isnull=True):
        category.save()
        count += 1
    for category in Category.objects.filter(slug__exact=''):
        category.save()
        count += 1
    return HttpResponse(f"<h1>Correction terminée.</h1><p>{count} catégories ont été corrigées.</p><a href='/'>Retour à l'accueil</a>")

def home_page(request):
    """
    View for the home page, which will display products and featured categories.
    """
    products = Product.objects.all().order_by('-id')[:8] # Get 8 most recent products

    context = {
        'products': products,
    }
    return render(request, 'shop/home.html', context)

def category_page(request, category_slug):
    """
    View for a category page, displaying products from that category.
    """
    try:
        # This assumes the Category model has a 'slug' field. 
        # If not, this will need to be adjusted.
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)
    except Category.DoesNotExist:
        category = None
        products = []
    
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/category.html', context)

def product_detail_page(request, pk):
    """
    View for a single product's detail page.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        product = None

    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)

@login_required
def cart_page(request):
    """
    View for the shopping cart page.
    """
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'shop/cart.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('shop:cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('shop:cart')

@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('shop:cart')

def producers_page(request):
    """
    View for the producers page.
    """
    # Producer logic will be added later
    return render(request, 'shop/producers.html')

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:home')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/update_product.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('shop:home')
    return render(request, 'shop/product_confirm_delete.html', {'product': product})