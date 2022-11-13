from rest_framework.decorators import action
from rest_framework.generics import (UpdateAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Clinic, Department
from .serializers import ClinicSerializer, DepartmentSerializer


class ClinicRetrieveApiView(RetrieveAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    permission_classes = [IsAuthenticated]


class ClinicUpdateApiView(UpdateAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    permission_classes = [IsAdminUser]


class ClinicCreateApiView(CreateAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    permission_classes = [IsAdminUser]


class ClinicDestroyApiView(DestroyAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    permission_classes = [IsAdminUser]


class DepartmentCreateApiView(CreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAdminUser]


class DepartmentRetrieveApiView(RetrieveAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated]


class DepartmentDestroyApiView(DestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAdminUser]

