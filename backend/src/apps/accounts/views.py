from rest_framework import generics
from apps.accounts.models import User
from .serializers import UserSerializer
from apps.accounts.permissions.base import IsAdmin


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]   # 🔥 PROTECTED