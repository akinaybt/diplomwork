from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import DoctorUserSerializer, DoctorProfileSerializer

from .models import DoctorProfile, DoctorUser
from .permissions import DoctorPermission


class DoctorProfileViewSet(viewsets.ModelViewSet):
    """
    DoctorProfileViewSet представление для модели DoctorProfile.
    Реализовывает CRUD(Create,Read,Update,Delete) для профиля доктора с разрешением ялвяется ли пользователь Доктором.
    Также здесь реализован поиск докторов по специальности.
    """
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    permission_classes = [DoctorPermission]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['department']


class DoctorUserListView(ListAPIView):
    """
    Представления DoctorUserListView для модели DoctorUser. Реализован поиск докторов по имени и фамилии.
    """
    queryset = DoctorUser.objects.all()
    serializer_class = DoctorUserSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['user__first_name', 'user__last_name']
