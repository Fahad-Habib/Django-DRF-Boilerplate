"""API URLs of the users app."""

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.api.views import (ChangePasswordAPIView, UserActivationAPIView,
                             UserSignUpAPIView)

urlpatterns = [
    path('signup/', UserSignUpAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('password/change/', ChangePasswordAPIView.as_view()),
    path('confirm-email/<uid>/<token>/', UserActivationAPIView.as_view()),
]
