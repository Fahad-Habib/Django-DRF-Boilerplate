"""Forms of the users app."""

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from users.tokens import CustomTokenGenerator

User = get_user_model()
Token_Generator = CustomTokenGenerator()
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
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = PLACE_HOLDERS[field]
            self.fields[field].label = ''
            self.fields[field].help_text = None

    def save(self, commit=True):
        """Send activation email after creating the user."""
        user = super().save(commit)
        self.send_activation_email(user)
        return user

    def send_activation_email(self, user):
        """Send activation email."""
        html_message = render_to_string('activation_email.html', {
            'domain': get_current_site(self.request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': Token_Generator.make_token(user),
        })
        send_mail(
            subject='Activate your account',
            message='Thank you for registering an account with us!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            html_message=html_message
        )
