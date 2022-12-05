from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework.decorators import action

from .models import Card, MakeAppointment
from .serializers import CardSerializer, MakeAppointmentSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

#
# class CardCreateAPIView(generics.CreateAPIView):
#     """ Представление CardCreateAPIView необходимо для создания медицинской карточки пациента."""
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#
#
# class CardDestroyAPIView(generics.DestroyAPIView):
#     """ Представление CardDestroyAPIView необходимо для удаления медицинской карточки пациента."""
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#
#
# class CardRetrieveAPIView(generics.RetrieveAPIView):
#     """ Представление CardRetrieveAPIView необходимо для детального просмотра медицинской карточки пациента."""
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#
#
# class CardUpdateAPIView(generics.UpdateAPIView):
#     """ Представление CardUpdateAPIView необходимо для изменения медицинской карточки пациента."""
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#
#
# class CardListAPIView(generics.ListAPIView):
#     """ Представление CardListAPIView необходимо для списка всех созданных медицинскихкарточек пациентов."""
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer


class MakeAppointmentAPIView(generics.CreateAPIView):
    queryset = MakeAppointment.objects.all()
    serializer_class = MakeAppointmentSerializer

