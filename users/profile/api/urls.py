"""API URLs of the profile app."""

from django.urls import path

from users.profile.api import views

urlpatterns = [
    path('profile/', views.UserProfileAPIView.as_view()),
]
