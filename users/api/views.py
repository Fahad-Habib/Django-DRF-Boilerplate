"""API views of the users app."""

from rest_framework import generics

from users.api.serializers import UserSerializer


class UserSignUpView(generics.CreateAPIView):
    """User Sign Up API view."""

    serializer_class = UserSerializer
