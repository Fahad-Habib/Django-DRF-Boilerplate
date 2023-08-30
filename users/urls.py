"""URLs of the users app."""

from django.urls import include, path

from users.views import (UserActivationView, UserLoginView, UserLogoutView,
                         UserSignupView)

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('password/', include('users.passwords.urls')),

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('activate/<uid>/<token>/', UserActivationView.as_view(), name='activate')
]
