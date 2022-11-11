from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('user-create/', views.UserProfileCreateView.as_view()),
    path('user-detail/', views.UserProfileDetailView.as_view()),
    path('user-list/', views.UserListView.as_view()),
]


