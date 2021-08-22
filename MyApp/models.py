from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_manager=models.BooleanField(default=False)

class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    start = models.DateField()
    end = models.DateField()
    value = models.DecimalField(max_digits=50, decimal_places=20)
