from django.db import models
from Courses.models import Courses


class CourseMaterials(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, related_name='course_material_id', on_delete=models.PROTECT)
    title = models.TextField()
    description = models.TextField()
    file_link = models.CharField()
