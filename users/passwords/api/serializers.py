"""Serializers of the passwords app."""

from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    """Change Password serializer."""

    old_password = serializers.CharField(min_length=8, max_length=100, required=True)
    new_password = serializers.CharField(min_length=8, max_length=100, required=True)
    confirm_password = serializers.CharField(min_length=8, max_length=100, required=True)
