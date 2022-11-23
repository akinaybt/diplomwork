from requests import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.generics import (ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView )
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .permissions import IsProfileOrReadOnly
from .serializers import UserProfileSerializer, CustomUserSerializer, AppointmentSerializer
from .models import CustomUser, UserProfile, Appointment
from doctor.serializers import ScheduleSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @action(detail=True, methods=['GET'], name='appointments', url_path='appointments')
    def get_schedule(self, request, *args, **kwargs):
        schedule = self.get_object()
        serializer = ScheduleSerializer(f"ВРемя работы: {schedule.start_time} - {schedule.end_time}", many=True)
        return Response(serializer.data)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserProfileCreateView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserListView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsProfileOrReadOnly, IsAuthenticated]


# class UserPasswordUpdateView(generics.UpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserPasswordSerializer


