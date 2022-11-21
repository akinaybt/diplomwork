from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import DoctorProfile, DoctorUser


@receiver(post_save, sender=DoctorUser)
def create_doctor_profile(sender, instance, created, **kwargs):
    if created:
        print('Doctor signal received!')
        DoctorProfile.objects.create(
            user=instance,
)

