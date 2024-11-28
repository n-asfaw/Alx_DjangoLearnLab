# advanced_features_and_security/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define the fields to display in the admin list view
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'date_of_birth')
    search_fields = ('username', 'email')
    ordering = ('username',)
    
    # Add fields to the form to edit user details
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )

# Register the custom user model with the admin
admin.site.register(CustomUser, CustomUserAdmin)

