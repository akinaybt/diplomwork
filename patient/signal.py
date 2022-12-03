from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, CustomUser
from doctor.models import DoctorUser


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('USER PROFILE HAS BEEN CREATED!')
    if not created:
        if not instance.is_patient:
            instance.profile.delete()
            DoctorUser.objects.create(
                user=instance
            )
            print('Doctor user has been created!')












