from django.db import models
from patient.models import UserProfile, Appointment


class MakeAppointment(models.Model):
    diagnosis = models.CharField(max_length=255, null=True)
    treatment = models.TextField(null=True)
    medicine = models.TextField(null=True)

    class Meta:
        verbose_name = 'Назначить приём'
        verbose_name_plural = 'Назначить приём'


class Card(models.Model):
    patient = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    allergies = models.CharField(max_length=100, null=True)
    birth_date = models.DateField()
    blood_group = models.CharField(max_length=20)
    appointment = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Медицинская карточка'
        verbose_name_plural = 'Медицинские карточки'

    def __str__(self):
        return f"Медицинская карточка {self.patient}"



