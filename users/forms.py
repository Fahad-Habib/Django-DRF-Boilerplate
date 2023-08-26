"""Forms of the users app."""

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

PLACE_HOLDERS = {
    'username': 'Email',
    'password': 'Password',
    'password1': 'Password',
    'password2': 'Confirm Password',
}


class UserLoginForm(AuthenticationForm):
    """User Log In Form."""

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = PLACE_HOLDERS[field]
            self.fields[field].label = ''
            self.fields[field].help_text = None


class UserSignupForm(UserCreationForm):
    """User Sign Up Form."""

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = PLACE_HOLDERS[field]
            self.fields[field].label = ''
            self.fields[field].help_text = None
