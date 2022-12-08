from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Clinic, Department
from .serializers import ClinicSerializer, DepartmentSerializer

from doctor.serializers import DoctorProfileSerializer


class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

    @action(detail=True, methods=['GET'], name='doctor', url_path='doctors_list')
    def get_appointment_detail(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = DoctorProfileSerializer(obj.doctors_profiles, many=True)
        print(obj.doctors_profiles)
        return Response(serializer.data)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
