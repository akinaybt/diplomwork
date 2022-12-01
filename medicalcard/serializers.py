from rest_framework import serializers
from patient.models import Appointment
from .models import Card
from patient.serializers import AppointmentSerializer


class CardSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()


    def get_patient_name(self, obj):
        return f"{obj.patient}"


    class Meta:
        model = Card
        fields = ('id', 'patient', 'patient_name', 'allergies', 'birth_date', 'blood_group')





