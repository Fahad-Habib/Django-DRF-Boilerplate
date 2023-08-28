"""Forms of the passwords app."""

from django.contrib.auth.forms import (PasswordChangeForm, PasswordResetForm,
                                       SetPasswordForm)

PLACE_HOLDERS = {
    'email': 'Enter your email',
    'old_password': 'Enter old password',
    'new_password1': 'New Password',
    'new_password2': 'Confirm Password'
}


class BaseForm:
    """Base form class."""

    def change_style(self):
        """Add styling to the fields."""
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = PLACE_HOLDERS[field]
            self.fields[field].label = ''
            self.fields[field].help_text = None


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
