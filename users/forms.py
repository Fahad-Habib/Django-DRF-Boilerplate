"""Forms of the users app."""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from core.forms import BaseForm
from users.mixins import EmailMixin

User = get_user_model()


class UserLoginForm(AuthenticationForm, BaseForm):
    """User Log In Form."""

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        self.change_style()


class UserSignupForm(UserCreationForm, EmailMixin, BaseForm):
    """User Sign Up Form."""

    class Meta:
        """Add model and fields."""

        model = User
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        self.change_style()

    def save(self, commit=True):
        """Send activation email after creating the user."""
        user = super().save(commit)
        self.send_activation_email(self.request, user)
        return user


class UserProfileForm(forms.ModelForm, BaseForm):
    """User Profile Form."""

    class Meta:
        """Define model and fields."""

        model = User
        fields = ['first_name', 'last_name', 'about', 'address', 'contact', 'picture']

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        self.change_style()
