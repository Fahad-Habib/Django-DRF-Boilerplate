"""Views of the users app."""

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserLoginForm, UserSignupForm
from users.mixins import OnlyUnauthenticatedMixin

User = get_user_model()


class UserLoginView(OnlyUnauthenticatedMixin, SuccessMessageMixin, LoginView):
    """User Log In View."""

    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')
    success_message = 'Logged in successfully!'

    def get_success_url(self):
        """Return success url."""
        return reverse_lazy('home')


class UserSignupView(OnlyUnauthenticatedMixin, SuccessMessageMixin, CreateView):
    """User Sign Up View."""

    template_name = 'signup.html'
    form_class = UserSignupForm
    success_url = reverse_lazy('login')
    success_message = 'Signed up successfully!'

    def get_form_kwargs(self):
        """Send request to the form."""
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class UserLogoutView(LoginRequiredMixin, SuccessMessageMixin, LogoutView):
    """User Log Out View."""

    success_message = 'You have been logged out.'

    def get_success_url(self):
        """Return success url."""
        return reverse_lazy('home')
