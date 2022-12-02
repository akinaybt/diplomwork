from rest_framework import fields, serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import DoctorProfile, Schedule, DoctorUser, WEEKDAYS


class PhoneNumberSerializer(serializers.Serializer):
    number = PhoneNumberField(region='KG')


class DoctorProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    department_name = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return f"{obj.user}"

    def get_department_name(self, obj):
        return f"{obj.department}"

    class Meta:
        model = DoctorProfile
        fields = (
            'id',
            'user',
            'user_name',
            'department',
            'department_name',
            'experience',
        )


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = (
            'id',
            'weekday',
            'start_time',
            'end_time',
        )


class DoctorUserSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()

    def get_doctor_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    class Meta:
        model = DoctorUser
        fields = '__all__'



# class MyModelSerializer(serializers.HyperlinkedModelSerializer):
#     # ...
#     my_field = fields.MultipleChoiceField(choices=MY_CHOICES)
#     my_field2 = fields.MultipleChoiceField(choices=MY_CHOICES2)
#     # ...