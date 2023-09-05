"""API URLs of the users app."""

from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.api import views

urlpatterns = [
    path('profile/', include('users.profile.api.urls')),
    path('password/', include('users.passwords.api.urls')),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('signup/', views.UserSignUpAPIView.as_view()),
    path('confirm-email/<uid>/<token>/', views.UserActivationAPIView.as_view()),
]
