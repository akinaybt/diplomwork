from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('clinic', views.ClinicViewSet)
router.register('departments', views.DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
