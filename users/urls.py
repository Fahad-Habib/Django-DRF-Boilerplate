from django.urls import path
from users.views import UserLoginView

urlpatterns = [
    path('', UserLoginView.as_view(), name='home'),  # Home View to be created later
    path('login/', UserLoginView.as_view(), name='login')
]
