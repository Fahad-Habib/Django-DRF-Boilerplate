"""URLs of the users app."""

from django.urls import path

from users.views import UserLoginView, UserLogoutView, UserSignupView

urlpatterns = [
    path('', UserSignupView.as_view(), name='home'),  # Home View to be created later
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', UserSignupView.as_view(), name='signup')
]
