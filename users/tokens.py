"""Custom Token Generator."""

from django.contrib.auth.tokens import PasswordResetTokenGenerator


class CustomTokenGenerator(PasswordResetTokenGenerator):
    """Generate Custom Tokens based on user data."""

    def _make_hash_value(self, user, timestamp):
        """Generate a hash value for the token using user-specific data."""
        return f"{user.pk}{user.email}{timestamp}"
