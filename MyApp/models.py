from django.db import models
from datetime import date


class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    start = models.DateField()
    end = models.DateField()
    value = models.DecimalField(max_digits=50, decimal_places=20)
