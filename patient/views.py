from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .permissions import IsProfileOrReadOnly
from .serializers import UserProfileSerializer, CustomUserSerializer, AppointmentSerializer
from .models import CustomUser, UserProfile, Appointment
from doctor.serializers import ScheduleSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """Представление AppointmentViewSet создано для модели AppointmentViewS"""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'], name='schedule', url_path='schedule')
    def get_schedule(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = ScheduleSerializer(obj.schedule)
        return Response(serializer.data)


class CustomUserViewSet(viewsets.ModelViewSet):
    """Представление CustomUserViewSet написано для модели CustomUser. """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """Представление UserProfileViewSet создано для модели UserProfile. """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileOrReadOnly]
