"""Views of the passwords app."""

from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from users.passwords.forms import (CustomPasswordChangeForm,
                                   CustomPasswordResetForm,
                                   CustomSetPasswordForm)


class CustomPasswordResetView(auth_views.PasswordResetView):
    """Customize Password Reset View."""

    template_name = 'reset_password.html'
    form_class = CustomPasswordResetForm


class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    """Customize Password Reset Done View."""

    template_name = 'password_reset_done.html'


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """Customize Password Reset Confirm View."""

    template_name = 'password_reset_confirm.html'
    form_class = CustomSetPasswordForm


class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    """Customize Password Reset Complete View."""

    template_name = 'password_reset_complete.html'


class CustomPasswordChangeView(SuccessMessageMixin, auth_views.PasswordChangeView):
    """Customize Password Change View."""

    template_name = 'change_password.html'
    form_class = CustomPasswordChangeForm
    success_message = 'Password changed successfully.'
    success_url = reverse_lazy('home')
