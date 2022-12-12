from django.db import models


class Clinic(models.Model):
    """Модель Clinic предназначена для создания Больницы города."""
    title = models.CharField(max_length=200, null=False, blank=True)
    foundation_date = models.DateField()
    hospital_director = models.CharField(max_length=100, null=False, blank=True)

    class Meta:
        verbose_name = 'Клиника'
        verbose_name_plural = 'Клиники'

    def __str__(self):
        return self.title


class Department(models.Model):
    """Модель Department предназначена для создания отделений Больницы. """
    clinic = models.ForeignKey(Clinic, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, null=False, blank=True)
    head_doctor = models.CharField(max_length=100, null=False, blank=True)

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    def __str__(self):
        return self.title
