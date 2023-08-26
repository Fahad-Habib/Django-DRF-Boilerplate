"""API views of the users app."""

from rest_framework.generics import CreateAPIView

from users.api.serializers import UserSerializer


class UserSignUpView(CreateAPIView):
    """User Sign Up API view."""

    serializer_class = UserSerializer
