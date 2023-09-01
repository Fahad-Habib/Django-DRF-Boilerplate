"""Forms of the profile app."""

from django import forms
from django.contrib.auth import get_user_model

from core.forms import BaseForm

User = get_user_model()


class UserProfileForm(forms.ModelForm, BaseForm):
    """User Profile Form."""

    class Meta:
        """Define model and fields."""

        model = User
        fields = ['first_name', 'last_name', 'handle', 'about', 'address', 'contact', 'picture']

    def __init__(self, *args, **kwargs):
        """Add styling to the fields."""
        super().__init__(*args, **kwargs)

        self.change_style()
