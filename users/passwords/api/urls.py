"""API URLs of the passwords app."""

from django.urls import path

from users.passwords.api import views

urlpatterns = [
    path('change/', views.ChangePasswordAPIView.as_view()),
]
