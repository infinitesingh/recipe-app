from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models

# Register your models here.

# admin.site.register(models.User)


""" Customize the admin page"""

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']

admin.site.register(models.User, UserAdmin)
