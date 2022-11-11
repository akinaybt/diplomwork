from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from doctor.models import Doctor, Department
import phonenumbers


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=30, blank=True, null=False)
    marital_status = models.CharField(max_length=30, blank=True, null=False)
    phone_number = PhoneNumberField(null=True, unique=True, region='KG')

    def __str__(self):
        """Returns the patient's full name."""
        return '%s %s' % (self.first_name, self.last_name)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')


# class Appointment(models.Model):
#     referred_department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     referred_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # appointment_date = models.DateTimeField()
    # appointment_time =
