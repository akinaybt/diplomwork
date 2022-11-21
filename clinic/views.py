from rest_framework.generics import (UpdateAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Clinic, Department
from .serializers import ClinicSerializer, DepartmentSerializer
from rest_framework import viewsets


class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
