from django.db import models


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
