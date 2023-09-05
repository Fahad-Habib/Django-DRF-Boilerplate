"""Forms of the passwords app."""

from django.contrib.auth.forms import (PasswordChangeForm, PasswordResetForm,
                                       SetPasswordForm)

from core.forms import BaseForm


class CustomPasswordResetForm(PasswordResetForm, BaseForm):
    """Customize Password Reset Form."""

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        self.change_style()


class CustomSetPasswordForm(SetPasswordForm, BaseForm):
    """Customize Set Password Form."""

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        self.change_style()


class CustomPasswordChangeForm(PasswordChangeForm, BaseForm):
    """Customize Password Reset Form."""

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        self.change_style()
