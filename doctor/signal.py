from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DoctorProfile, DoctorUser


@receiver(post_save, sender=DoctorUser)
def create_doctor_profile(sender, instance, created, **kwargs):
    """ Сигнал, который автоматически создаёт объект модели DoctorUser. """
    if created:
        print('Doctor signal received!')
        DoctorProfile.objects.create(
            user=instance,
        )
