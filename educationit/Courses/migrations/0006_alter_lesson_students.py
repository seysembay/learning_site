# Generated by Django 5.0.3 on 2024-03-20 17:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0005_lesson_students'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='students',
            field=models.ManyToManyField(blank=True, db_column='student_id', related_name='course_lessons', to=settings.AUTH_USER_MODEL),
        ),
    ]