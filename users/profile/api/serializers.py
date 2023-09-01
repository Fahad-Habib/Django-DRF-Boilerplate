"""Serializers of the profile app."""

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    """User Profile Serializer."""

    class Meta:
        """Define model and fields."""

        model = User
        fields = ['first_name', 'last_name', 'handle', 'about', 'address', 'contact', 'picture']
        extra_kwargs = {'handle': {'required': False}}
