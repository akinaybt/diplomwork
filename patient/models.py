# from django.db import models
# from doctor.models import Doctor, Department
#
#
# class PatientInfo(models.Model):
#     name = models.CharField(max_length=50, blank=True, null=False)
#     gender = models.CharField(max_length=200, blank=True, null=False)
#     marital_Status = models.CharField(max_length=100, blank=True, null=False)
#     telephone = models.CharField(max_length=30, blank=True, null=False)
#
#
# class Appointment(models.Model):
#     referred_department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     referred_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     # appointment_date = models.DateTimeField()
#     # appointment_time =
