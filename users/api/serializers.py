"""Serializers of the users app."""

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.mixins import EmailMixin

User = get_user_model()


class UserSerializer(serializers.ModelSerializer, EmailMixin):
    """User serializer."""

    confirm_password = serializers.CharField(min_length=8, max_length=100, write_only=True, required=True)

    class Meta:
        """Define model and fields."""

        model = User
        fields = ('id', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}, 'id': {'read_only': True}}

    def __init__(self, *args, **kwargs):
        """Initialize."""
        self.request = kwargs['context']['request']
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        """Create new user."""
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data.pop('password'))
        user = User.objects.create(**validated_data)
        self.send_activation_email(self.request, user)
        return user

    def validate(self, attrs):
        """Validate passwords."""
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def to_representation(self, instance):
        """Include message in the response."""
        data = super().to_representation(instance)
        data.update({
            "message": "Verification email has been sent to your email address. Please check your inbox or spam folder."
        })
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    """User Profile Serializer."""

    class Meta:
        """Define model and fields."""

        model = User
        fields = ['first_name', 'last_name', 'about', 'address', 'contact', 'picture']


class ChangePasswordSerializer(serializers.Serializer):
    """Change Password serializer."""

    old_password = serializers.CharField(min_length=8, max_length=100, required=True)
    new_password = serializers.CharField(min_length=8, max_length=100, required=True)
    confirm_password = serializers.CharField(min_length=8, max_length=100, required=True)
