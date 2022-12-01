from rest_framework import serializers
from .models import Clinic, Department


class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'title', 'head_doctor')


