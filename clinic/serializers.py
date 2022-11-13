from rest_framework import serializers
from .models import Clinic, Department


class ClinicSerializer(serializers.Serializer):

    class Meta:
        model = Clinic
        fields = '__all__'


class DepartmentSerializer(serializers.Serializer):

    class Meta:
        model = Department
        fields = '__all__'


