from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Card
from .serializers import CardSerializer


class CardCreateAPIView(generics.CreateAPIView):
    """ Представление CardCreateAPIView необходимо для создания медицинской карточки пациента."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]


class CardDestroyAPIView(generics.DestroyAPIView):
    """ Представление CardDestroyAPIView необходимо для удаления медицинской карточки пациента."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]


class CardRetrieveAPIView(generics.RetrieveAPIView):
    """ Представление CardRetrieveAPIView необходимо для детального просмотра медицинской карточки пациента."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]


class CardUpdateAPIView(generics.UpdateAPIView):
    """ Представление CardUpdateAPIView необходимо для изменения медицинской карточки пациента."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]


class CardListAPIView(generics.ListAPIView):
    """ Представление CardListAPIView необходимо для списка всех созданных медицинскихкарточек пациентов."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

