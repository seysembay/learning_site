from django.db import models
from django.utils import timezone

from Users.models import CustomUser


class Courses(models.Model):
    DURATION_UNIT_CHOICES = (
        ('weeks', 'недель'),
        ('months', 'месяцев'),
        ('years', 'лет'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    description = models.TextField()
    duration = models.IntegerField()
    duration_unit = models.CharField(choices=DURATION_UNIT_CHOICES, default='months')
    icon_link = models.CharField(null=True)
    teacher = models.ForeignKey(CustomUser, related_name='course_teacher_id', on_delete=models.PROTECT, default=1,
                                null=False)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
