from rest_framework.permissions import BasePermission


class DoctorPermission(BasePermission):
    def has_permission(self, request, view):
        """ Permission class, написанный кастомно для модели DoctorUser. Пользователь должен иметь объект пользователя,
        связанный с моделью DoctorUser, чтобы иметь доступ к данным"""
        return bool(request.user and hasattr(request.user, 'doctoruser'))
