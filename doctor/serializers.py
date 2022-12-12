from rest_framework import serializers
from .models import DoctorProfile, Schedule, DoctorUser


class DoctorProfileSerializer(serializers.ModelSerializer):
    """
    DoctorProfileSerializer сериалайзер, написанный для модели DoctorProfile.
    Нужен для преобразования данных модели DoctorProfile в формат JSON.
    """
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
    """
    ScheduleSerializer сериалайзер, написанный для модели Schedule.
    Нужен для преобразования данных модели Schedule в формат JSON.
    """
    class Meta:
        model = Schedule
        fields = (
            'id',
            'weekday',
            'start_time',
            'end_time',
        )


class DoctorUserSerializer(serializers.ModelSerializer):
    """
    DoctorUserSerializer сериалайзер, написанный для модели DoctorUser.
    Нужен для преобразования данных модели Doctor в формат JSON.
    """
    doctor_name = serializers.SerializerMethodField()

    def get_doctor_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    class Meta:
        model = DoctorUser
        fields = '__all__'
