from django.db import models


class Clinic(models.Model):
    title = models.CharField(max_length=200)
    foundation_date = models.DateField()

    def __str__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(max_length=200)
    clinic = models.ForeignKey('Clinic', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


