"""Views of the passwords app."""

from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import reverse_lazy

from users.passwords.forms import (CustomPasswordChangeForm,
                                   CustomPasswordResetForm,
                                   CustomSetPasswordForm)


class CustomPasswordResetView(PasswordResetView):
    """Customize Password Reset View."""

    template_name = 'reset_password.html'
    form_class = CustomPasswordResetForm


class CustomPasswordResetDoneView(PasswordResetDoneView):
    """Customize Password Reset Done View."""

    template_name = 'password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """Customize Password Reset Confirm View."""

    template_name = 'password_reset_confirm.html'
    form_class = CustomSetPasswordForm


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """Customize Password Reset Complete View."""

    template_name = 'password_reset_complete.html'


class CustomPasswordChangeView(PasswordChangeView):
    """Customize Password Change View."""

    template_name = 'change_password.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('home')
