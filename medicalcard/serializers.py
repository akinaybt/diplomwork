from rest_framework import serializers
from .models import Card, MakeAppointment


class CardSerializer(serializers.ModelSerializer):
    """ CardSerializer сериалайзер для модели Card"""
    patient_name = serializers.SerializerMethodField()

    def get_patient_name(self, obj):
        return f"{obj.patient}"

    class Meta:
        model = Card
        fields = (
            'id',
            'patient',
            'patient_name',
            'allergies',
            'birth_date',
            'blood_group',
            'appointment',
        )


class MakeAppointmentSerializer(serializers.ModelSerializer):
    """ MakeAppointmentSerializer сериалайзер для модели MakeAppointment"""
    class Meta:
        model = MakeAppointment
        fields = (
            'id',
            'diagnosis',
            'treatment',
            'medicine',
        )
