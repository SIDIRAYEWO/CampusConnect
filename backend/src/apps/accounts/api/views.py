from rest_framework import generics, permissions
from apps.accounts.models import User
from .serializers import UserSerializer
from apps.accounts.permissions.base import IsAdmin


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]  # 🔥 allow user creation
        return [IsAdmin()]  # 🔐 only admin can view list