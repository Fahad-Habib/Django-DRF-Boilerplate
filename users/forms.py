"""Forms of the users app."""

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()
PLACE_HOLDERS = {
    'email': 'Email',
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

    class Meta:
        """Add model and fields."""

        model = User
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = PLACE_HOLDERS[field]
            self.fields[field].label = ''
            self.fields[field].help_text = None
