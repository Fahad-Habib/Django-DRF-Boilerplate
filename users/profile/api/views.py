"""API views of the profile app."""

from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from users.profile.api.serializers import UserProfileSerializer

User = get_user_model()


class UserProfileAPIView(RetrieveAPIView, UpdateAPIView):
    """User Profile API View."""

    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        """Allow users to only change their own profile."""
        return self.request.user
