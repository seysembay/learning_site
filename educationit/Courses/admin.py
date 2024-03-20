from django.contrib import admin

from .models import Courses, Lesson, CourseStudent


class CourseStudentsInline(admin.TabularInline):
    model = Courses.students.through
    extra = 1


@admin.register(Courses)
class Courses(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', 'duration_unit', 'teacher', 'get_students')
    inlines = [CourseStudentsInline]

    def get_students(self, obj):
        return ", ".join([student.email for student in obj.students.all()])

    get_students.short_description = 'Students'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'published_date')
    list_filter = ('course', 'published_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'published_date'
