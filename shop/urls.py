from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('__fix-slugs__/', views.fix_slugs, name='fix_slugs'), # Temporary URL to fix slugs
    path('', views.home_page, name='home'),
    path('category/<slug:category_slug>/', views.category_page, name='category'),
    path('product/<int:pk>/', views.product_detail_page, name='product_detail'),
    path('cart/', views.cart_page, name='cart'),
    path('producers/', views.producers_page, name='producers'),
    path('add-product/', views.add_product, name='add_product'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('product/<int:pk>/update/', views.update_product, name='update_product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
]