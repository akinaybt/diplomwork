from django.conf import settings
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class PhoneNumberSerializer(serializers.Serializer):
    number = PhoneNumberField(region='KG')