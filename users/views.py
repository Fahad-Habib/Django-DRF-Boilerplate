from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from users.forms import UserLoginForm


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')
