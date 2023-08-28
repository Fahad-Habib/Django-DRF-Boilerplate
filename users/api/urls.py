"""API URLs of the users app."""

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.api.views import UserSignUpAPIView, ChangePasswordAPIView

urlpatterns = [
    path('signup/', UserSignUpAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('password/change/', ChangePasswordAPIView.as_view())
]
