"""URLs of the core app."""

from django.urls import path

from core.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
