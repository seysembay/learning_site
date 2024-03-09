from django.contrib import admin
from .models import CustomUser, Role


@admin.register(CustomUser)
class User(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role')


@admin.register(Role)
class User(admin.ModelAdmin):
    list_display = ('id', 'name')
