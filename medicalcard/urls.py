from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('card-create/', views.CardCreateAPIView.as_view()),
    path('card-update/', views.CardUpdateAPIView.as_view()),
    path('card-retrieve/', views.CardRetrieveAPIView.as_view()),
    path('card-destroy/', views.CardDestroyAPIView.as_view()),
    path('card-list/', views.CardListAPIView.as_view())
]

