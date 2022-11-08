from django.db import models
from clinic.models import Department


class Doctor(models.Model):
    department = models.OneToOneField(Department, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    experience = models.PositiveIntegerField()


class Schedule(models.Model):
    doctor = models.OneToOneField('Doctor', on_delete=models.CASCADE)
    WEEKDAYS = [
        ('Пн', 'Понедельник'),
        ('Вт', 'Вторник'),
        ('Ср', 'Среда'),
        ('Чт', 'Четверг'),
        ('Пт', 'Пятница'),
        ('Сб', 'Суббота'),
        ('Вс', 'Воскресенье'),
             ]
    weekday = models.IntegerField(choices=WEEKDAYS)
    # working_time = models.DurationField()



# import datetime as datetime_class # забыл добавить в ответ
#
# duration = datetime.strptime(duration, "%H:%M")
# x_duration =datetime_class.timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second).total_seconds()
# duration = timedelta(seconds = x_duration)



