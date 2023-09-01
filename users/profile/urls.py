"""URLs of the profile app."""

from django.urls import path

from users.profile import views

urlpatterns = [
    path('<str:handle>/', views.UserProfileView.as_view(), name='user_profile'),
    path('<str:handle>/edit/', views.UserProfileEditView.as_view(), name='edit_user_profile'),
]
