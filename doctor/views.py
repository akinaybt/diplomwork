from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .serializers import DoctorUserSerializer, DoctorProfileSerializer

from .models import DoctorProfile, DoctorUser


class DoctorProfileViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer


class DoctorUserListView(ListAPIView):
    queryset = DoctorUser.objects.all()
    serializer_class = DoctorUserSerializer
