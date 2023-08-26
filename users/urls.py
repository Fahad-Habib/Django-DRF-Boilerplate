from django.urls import path
from users.views import UserLoginView, UserSignupView

urlpatterns = [
    path('', UserLoginView.as_view(), name='home'),  # Home View to be created later
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserSignupView.as_view(), name='signup')
]
