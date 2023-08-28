"""Forms of the passwords app."""

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

PLACE_HOLDERS = {
    'email': 'Enter your email',
    'new_password1': 'New Password',
    'new_password2': 'Confirm Password'
}


class CustomPasswordResetForm(PasswordResetForm):
    """Customize Password Reset Form."""

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = PLACE_HOLDERS[field]
            self.fields[field].label = ''
            self.fields[field].help_text = None


class CustomSetPasswordForm(SetPasswordForm):
    """Customize Set Password Form."""

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = PLACE_HOLDERS[field]
            self.fields[field].label = ''
            self.fields[field].help_text = None
