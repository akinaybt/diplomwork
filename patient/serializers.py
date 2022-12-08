from django.contrib.auth.hashers import make_password
from django.utils.timezone import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import validators

from doctor.models import Schedule
from .models import UserProfile, CustomUser, Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    department_title = serializers.SerializerMethodField()
    doctor_name = serializers.SerializerMethodField()
    schedule_name = serializers.SerializerMethodField()

    def get_patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"

    def get_department_title(self, obj):
        return f"{obj.referred_department}"

    def get_doctor_name(self, obj):
        return f"{obj.referred_doctor}"

    def get_schedule_name(self, obj):
        return f"{obj.schedule}"

    def validate(self, data):
        appointment_time = data.get('appointment_time')
        schedule = data.get('schedule')
        appointment_date = data.get('appointment_date')

        if not (appointment_time >= schedule.start_time and appointment_time <= schedule.end_time):
            raise ValidationError(
                {
                    'appointment_time': 'Выбранное Вами время является неподходящим, так как доктор в это время не работает'
                }
            )
        appointment_detail = Appointment.objects.filter(
            appointment_time=appointment_time,
            appointment_date=appointment_date,
            referred_doctor=schedule.doctor
        ).exists()
        if appointment_detail:
            raise ValidationError(
                {
                    'appointment_time': 'Назначение на это время уже существует. Выберите другое время.'
                }
            )
        return data

    class Meta:
        model = Appointment
        fields = (
            'patient_name',
            'patient',
            'department_title',
            'referred_department',
            'doctor_name',
            'referred_doctor',
            'schedule',
            'schedule_name',
            'appointment_date',
            'appointment_time',
            'confirm_appointment',
        )


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'phone_number'
        )

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(CustomUserSerializer, self).create(validated_data)


class PhoneNumberSerializer(serializers.Serializer):
    number = PhoneNumberField(region='KG')


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
