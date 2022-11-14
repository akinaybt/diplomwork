from django.db import models
from patient.models import UserProfile


class Allergy(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


class Card(models.Model):
    patient = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    allergies = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    birth_date = models.DateField()
    blood_group = models.CharField(max_length=20)


