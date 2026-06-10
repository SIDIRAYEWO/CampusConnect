from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.accounts.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        # Check lockout
        if user.locked_until and user.locked_until > timezone.now():
            raise serializers.ValidationError(
                "Account is locked. Try again later."
            )

        authenticated_user = authenticate(
            username=username,
            password=password
        )

        if authenticated_user is None:
            user.failed_login_attempts += 1

            if user.failed_login_attempts >= 5:
                user.locked_until = timezone.now() + timedelta(minutes=15)

            user.save()

            raise serializers.ValidationError("Invalid credentials")

        # Successful login
        user.failed_login_attempts = 0
        user.locked_until = None
        user.save()

        return super().validate(attrs)