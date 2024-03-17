from django.contrib import admin

from .models import Courses, Lesson


@admin.register(Courses)
class Courses(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', 'duration_unit')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'published_date')
    list_filter = ('course', 'published_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'published_date'
