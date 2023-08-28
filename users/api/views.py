"""API views of the users app."""

from rest_framework import response, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from users.api.serializers import UserSerializer, ChangePasswordSerializer


class UserSignUpAPIView(CreateAPIView):
    """User Sign Up API view."""

    serializer_class = UserSerializer


class ChangePasswordAPIView(APIView):
    """Change User password with APIs."""

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """Validate and update the password."""
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']
        confirm_password = serializer.validated_data['confirm_password']

        if not user.check_password(old_password):
            return response.Response({'details': 'Incorrect old password'}, status=status.HTTP_400_BAD_REQUEST)

        if new_password != confirm_password:
            return response.Response({'details': 'New passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return response.Response({'details': 'Password changed successfully'}, status=status.HTTP_200_OK)
