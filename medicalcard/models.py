from django.db import models
from patient.models import UserProfile


class Card(models.Model):
    patient = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    allergies = models.CharField(max_length=100, null=True)
    birth_date = models.DateField()
    blood_group = models.CharField(max_length=20)

    def __str__(self):
        return f"Медицинская карточка {self.patient}"

