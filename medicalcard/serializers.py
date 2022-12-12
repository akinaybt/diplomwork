from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    """
    CardSerializer сериалайзер для модели Card.
    Нужен для преобразования данных модели Card в формат JSON.
    """
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
