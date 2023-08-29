"""Views of the users app."""

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from users.forms import UserLoginForm, UserSignupForm
from users.mixins import OnlyUnauthenticatedMixin
from users.tokens import CustomTokenGenerator

User = get_user_model()
Token_Generator = CustomTokenGenerator()


class UserLoginView(OnlyUnauthenticatedMixin, SuccessMessageMixin, LoginView):
    """User Log In View."""

    template_name = 'login.html'
    form_class = UserLoginForm
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


class UserActivationView(TemplateView):
    """User Activation View."""

    template_name = 'activation.html'

    def get_context_data(self, **kwargs):
        """Verify token."""
        context = super().get_context_data(**kwargs)
        try:
            user_id = force_str(urlsafe_base64_decode(kwargs['uid']))
            user = User.objects.get(pk=user_id)
            if Token_Generator.check_token(user, kwargs['token']):
                if not user.is_verified:
                    user.is_verified = True
                    user.save()
                    context['activation_status'] = 'success'
                else:
                    context['activation_status'] = 'verified'
            else:
                context['activation_status'] = 'error'
        except Exception as e:
            context['activation_status'] = 'error'
        return context
