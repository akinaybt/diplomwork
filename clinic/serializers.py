from rest_framework import serializers
from .models import Clinic, Department


class ClinicSerializer(serializers.ModelSerializer):
    """
    ClinicSerializer сериалайзер для модели Clinic.
    Нужен для преобразования данных модели Clinic в формат JSON.
    """
    class Meta:
        model = Clinic
        fields = ('title', 'foundation_date', 'hospital_director')


class DepartmentSerializer(serializers.ModelSerializer):
    """
    DepartmentSerializer сериалайзер для модели Department.
    Нужен для преобразования данных модели Department в формат JSON.
    """
    class Meta:
        model = Department
        fields = ('id', 'title', 'head_doctor')
