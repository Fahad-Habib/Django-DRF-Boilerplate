"""API views of the users app."""

from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import response, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from users.api.serializers import ChangePasswordSerializer, UserSerializer
from users.tokens import CustomTokenGenerator

User = get_user_model()
Token_Generator = CustomTokenGenerator()


class UserSignUpAPIView(CreateAPIView):
    """User Sign Up API view."""

    serializer_class = UserSerializer


class UserActivationAPIView(APIView):
    """User Activation API View."""

    def get(self, request, *args, **kwargs):
        """Verify token and activate account."""
        try:
            user_id = force_str(urlsafe_base64_decode(kwargs['uid']))
            user = User.objects.get(pk=user_id)
            if Token_Generator.check_token(user, kwargs['token']):
                if not user.is_verified:
                    user.is_verified = True
                    user.save()
                    return response.Response({'message': 'Verification successful.'}, status=status.HTTP_200_OK)
                else:
                    return response.Response({'message': 'Account is already verified.'}, status=status.HTTP_200_OK)
            return response.Response({'message': 'Invalid or expired link.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return response.Response({'message': 'Invalid or expired link.'}, status=status.HTTP_400_BAD_REQUEST)


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
            return response.Response({'details': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)

        if new_password != confirm_password:
            return response.Response({'details': 'New passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return response.Response({'details': 'Password changed successfully.'}, status=status.HTTP_200_OK)
