from django.db import models


class Clinic(models.Model):
    title = models.CharField(max_length=200, null=False, blank=True)
    foundation_date = models.DateField()
    hospital_director = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.title


class Department(models.Model):
    clinic = models.ForeignKey('Clinic', on_delete=models.PROTECT)
    title = models.CharField(max_length=200, null=False, blank=True)
    head_doctor = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.title


