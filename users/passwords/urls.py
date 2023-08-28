"""URLs of the passwords app."""

from django.urls import path

from users.passwords.views import (CustomPasswordResetCompleteView,
                                   CustomPasswordResetConfirmView,
                                   CustomPasswordResetDoneView,
                                   CustomPasswordResetView)

urlpatterns = [
    path('reset/', CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset/sent/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
