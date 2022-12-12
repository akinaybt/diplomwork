from django.conf import settings
from django.db import models
from multiselectfield import MultiSelectField
from clinic.models import Department, Clinic


class DoctorUser(models.Model):
    """Модель DoctorUser предназначена для переопределения пользователя от модели CustomUser. """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        """Возвращает полное имя доктора. """
        return f'{self.user}'


class DoctorProfile(models.Model):
    """Модель DoctorProfile предназначена для профиля доктора."""
    user = models.OneToOneField(DoctorUser, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='doctors_profiles', null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)
    experience = models.PositiveIntegerField(default=2)

    class Meta:
        verbose_name = 'Профиль доктора'
        verbose_name_plural = 'Профили докторов'

    def __str__(self):
        """Возвращает полное имя доктора"""
        return f"{self.user}"


WEEKDAYS = (
    ('Пн', 'Понедельник'),
    ('Вт', 'Вторник'),
    ('Ср', 'Среда'),
    ('Чт', 'Четверг'),
    ('Пт', 'Пятница'),
    ('Сб', 'Суббота'),
    ('Вс', 'Воскресенье'),
)


class Schedule(models.Model):
    """ Модель Schedule нужна для того, чтобы доктор создавал свой график работы. """
    doctor = models.OneToOneField(DoctorProfile, on_delete=models.CASCADE)
    weekday = MultiSelectField(max_length=20, choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = 'График работы доктора'
        verbose_name_plural = 'Графики работы докторов'

    def __str__(self):
        """ Возвращает график, принадлежащий определённому доктору."""
        return f"График доктора - {self.doctor}"
