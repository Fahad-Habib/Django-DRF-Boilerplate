"""URLs of the passwords app."""

from django.urls import path

from users.passwords import views

urlpatterns = [
    path('reset/', views.CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset/sent/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change/', views.CustomPasswordChangeView.as_view(), name='change_password'),
]
