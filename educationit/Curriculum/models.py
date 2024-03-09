from django.db import models
from Courses.models import Courses
from Users.models import CustomUser


class Curriculum(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, related_name='course_id', on_delete=models.PROTECT)
    teacher = models.ForeignKey(CustomUser, related_name='course_teacher', on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField
