from django.contrib import admin

from .models import Courses


@admin.register(Courses)
class Courses(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', 'duration_unit')


