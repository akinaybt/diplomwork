from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('doctors', views.DoctorProfileViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('doctors-list/', views.DoctorUserListView.as_view()),
]
