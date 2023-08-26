"""Views of the users app."""

from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserLoginForm, UserSignupForm


class UserLoginView(SuccessMessageMixin, LoginView):
    """User Lg In View."""

    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')
    success_message = 'Logged in successfully!'


class UserSignupView(SuccessMessageMixin, CreateView):
    """User Sign Up View."""

    template_name = 'signup.html'
    form_class = UserSignupForm
    success_url = reverse_lazy('login')
    success_message = 'Signed up successfully!'
