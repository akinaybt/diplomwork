from django.conf import settings
from django.db import models
from multiselectfield import MultiSelectField
from clinic.models import Department
# from patient.models import CustomUser


class DoctorUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)


class DoctorProfile(models.Model):
    user = models.OneToOneField(DoctorUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.OneToOneField(Department, on_delete=models.PROTECT)
    experience = models.PositiveIntegerField()

    def __str__(self):
        """Returns the doctor's full name."""
        return '%s %s' % (self.name, self.last_name)


class Schedule(models.Model):
    doctor = models.OneToOneField('DoctorProfile', on_delete=models.CASCADE)
    WEEKDAYS = (
        ('Пн', 'Понедельник'),
        ('Вт', 'Вторник'),
        ('Ср', 'Среда'),
        ('Чт', 'Четверг'),
        ('Пт', 'Пятница'),
        ('Сб', 'Суббота'),
        ('Вс', 'Воскресенье'),
    )
    weekday = MultiSelectField(max_length=5, choices=WEEKDAYS)



