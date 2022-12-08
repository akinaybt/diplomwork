from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from doctor.models import DoctorProfile, Department, Schedule
import phonenumbers


class CustomUser(AbstractUser):
    """Модель CustomUser для регистрации пользователей."""
    is_patient = models.BooleanField(default=True)
    phone_number = PhoneNumberField(null=True, unique=True, region='KG')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class UserProfile(models.Model):
    """Модель UserProfile предназначена для профиля пользователя."""
    GENDER = (
        ('Male', "Мужчина"),
        ('Female', 'Женщина')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile',
                                primary_key=True)
    gender = models.CharField(max_length=30, choices=GENDER)
    phone_number = PhoneNumberField(null=True, unique=True, region='KG', verbose_name='Номер телефона')

    def __str__(self):
        """Возвращает полное имя пациента."""
        return f"{self.user}'s profile"


class Appointment(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    referred_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    referred_doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, null=False)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=False)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    confirm_appointment = models.BooleanField(default=False, null=False)

    def __str__(self):
        """Возвращает приём пациента."""
        return f"Приём у {self.patient}"


