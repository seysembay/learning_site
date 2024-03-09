from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    role = models.OneToOneField(Role, on_delete=models.CASCADE, related_name='user', null=True)
