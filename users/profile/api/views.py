"""API views of the profile app."""

from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound

from users.profile.api.serializers import UserProfileSerializer

User = get_user_model()


class UserProfileAPIView(RetrieveAPIView, UpdateAPIView):
    """User Profile API View."""

    serializer_class = UserProfileSerializer

    def get_permissions(self):
        """Allow only authenticated users to change their profile."""
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_object(self):
        """Allow users to only change their own profile."""
        try:
            user = User.objects.get(handle=self.kwargs['handle'])
            if self.request.method == 'GET':
                return user
            if user == self.request.user:
                return user
            else:
                raise NotFound()
        except User.DoesNotExist:
            raise NotFound()
