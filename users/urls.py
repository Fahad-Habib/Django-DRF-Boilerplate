"""URLs of the users app."""

from django.urls import include, path

from users import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('profile/', include('users.profile.urls')),
    path('password/', include('users.passwords.urls')),

    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('confirm-email/<uid>/<token>/', views.UserActivationView.as_view(), name='activate'),
]
