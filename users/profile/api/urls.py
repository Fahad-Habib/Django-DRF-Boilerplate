"""API URLs of the profile app."""

from django.urls import path

from users.profile.api import views

urlpatterns = [
    path('<str:handle>/', views.UserProfileAPIView.as_view()),
]
