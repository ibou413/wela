from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name in admin
    fields = ('name', 'slug', 'description', 'parent', 'Category_image')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')  # Ajout du champ shop
    list_filter = ('category',)  # Filtrage par catégorie et boutique
    search_fields = ('name', 'category__name')  # Recherche par nom, catégorie et nom de la boutique

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'total_amount')  # Corrected to use 'author' instead of 'user'
    list_filter = ('created_at',)
    search_fields = ('author__username',)  # Corrected to use 'author__username'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_filter = ('order', 'product')
    search_fields = ('order__id', 'product__name')

