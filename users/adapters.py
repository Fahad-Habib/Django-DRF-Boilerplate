"""Custom adapter."""

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
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
