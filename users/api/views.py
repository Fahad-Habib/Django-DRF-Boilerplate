from rest_framework import generics
from users.api.serializers import UserSerializer


class UserSignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer
