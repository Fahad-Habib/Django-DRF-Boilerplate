from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(min_length=8, max_length=100, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data.pop('password'))
        return User.objects.create(**validated_data)

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return attrs
