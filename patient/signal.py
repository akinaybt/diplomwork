from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import UserProfile, CustomUser
from doctor.models import DoctorProfile, DoctorUser


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

# @receiver(post_save, sender=CustomUser)
# def delete_profile_if_not_doctor(sender, created, instance, **kwargs):


# @receiver(post_save, sender=CustomUser)
# def create_doctor_user(sender, instance, created, **kwargs):
#     print('SIGNAL RECEIVED!')
    # if instance.is_doctor:
    #     DoctorUser.objects.create(user=instance)
    #     if created:
    #         DoctorProfile.objects.create(user=instance)









