"""Views of the passwords app."""

from django.contrib.auth.views import (PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)

from users.passwords.forms import (CustomPasswordResetForm,
                                   CustomSetPasswordForm)


class CustomPasswordResetView(PasswordResetView):
    """Customize Password Reset View."""

    form_class = CustomPasswordResetForm
    template_name = 'reset_password.html'


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
