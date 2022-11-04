from django.db import models
from clinic.models import Department


class Doctor(models.Model):
    department = models.OneToOneField(Department, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    experience = models.PositiveIntegerField()






