from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('appointments', views.AppointmentViewSet)
router.register('users', views.CustomUserViewSet)
router.register('user-profile', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),

]


