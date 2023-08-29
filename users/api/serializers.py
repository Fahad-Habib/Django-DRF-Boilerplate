"""Serializers of the users app."""

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers

from users.tokens import CustomTokenGenerator

User = get_user_model()
Token_Generator = CustomTokenGenerator()


class UserSerializer(serializers.ModelSerializer):
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
        self.send_activation_email(user)
        return user

    def validate(self, attrs):
        """Validate passwords."""
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

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

    def to_representation(self, instance):
        """Include message in the response."""
        data = super().to_representation(instance)
        data.update({
            "message": "Activation email has been sent to your email address. Please check your inbox or spam folder."
        })
        return data


class ChangePasswordSerializer(serializers.Serializer):
    """Change Password serializer."""

    old_password = serializers.CharField(min_length=8, max_length=100, required=True)
    new_password = serializers.CharField(min_length=8, max_length=100, required=True)
    confirm_password = serializers.CharField(min_length=8, max_length=100, required=True)
