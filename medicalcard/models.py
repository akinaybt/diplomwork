from django.db import models
from patient.models import UserProfile, Appointment


class Card(models.Model):
    """
    Модель Card нужна для создания медицинской карточки пользователя.
    """
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
