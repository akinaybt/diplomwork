from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters_
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from .serializers import DoctorUserSerializer, DoctorProfileSerializer

from .models import DoctorProfile, DoctorUser


class DoctorProfileViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer


class DoctorUserListView(ListAPIView):
    queryset = DoctorUser.objects.all()
    serializer_class = DoctorUserSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['user__first_name', 'user__last_name']

