from rest_framework import fields, serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import DoctorProfile, Schedule, DoctorUser, WEEKDAYS


class PhoneNumberSerializer(serializers.Serializer):
    number = PhoneNumberField(region='KG')


class DoctorProfileSerializer(serializers.Serializer):

    class Meta:
        model = DoctorProfile
        fields = '__all__'


class ScheduleSerializer(serializers.Serializer):
    weekday = fields.MultipleChoiceField(choices=WEEKDAYS)

    class Meta:
        model = Schedule
        fields = (
            'id',
            'weekday',
            'start_time',
            'end_time',
        )


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )



# class MyModelSerializer(serializers.HyperlinkedModelSerializer):
#     # ...
#     my_field = fields.MultipleChoiceField(choices=MY_CHOICES)
#     my_field2 = fields.MultipleChoiceField(choices=MY_CHOICES2)
#     # ...