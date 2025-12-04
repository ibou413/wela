from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets 

    

    list_display = ['username', 'first_name', 'last_name']
    list_filter = ['first_name']

admin.site.register(CustomUser, CustomUserAdmin)