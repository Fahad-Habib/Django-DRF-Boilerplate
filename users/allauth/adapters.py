"""Custom adapter."""

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

from users.mixins import EmailMixin

User = get_user_model()


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter, EmailMixin):
    """Custom adapter to handle social login."""

    def pre_social_login(self, request, sociallogin):
        """Connect social account to the user."""
        email = sociallogin.account.extra_data.get('email')

        if email:
            try:
                user = User.objects.get(email=email)
                sociallogin.connect(request, user)
            except User.DoesNotExist:
                pass

    def save_user(self, request, sociallogin, form=None):
        """Send activation email while creating user."""
        user = super().save_user(request, sociallogin, form)
        self.send_activation_email(request, user)
        return user
