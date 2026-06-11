# apps/accounts/api/urls.py

from django.urls import path
from .views import UserListCreateAPIView
from .logout_view import LogoutAPIView


urlpatterns = [
    path("users/", UserListCreateAPIView.as_view(), name="users"),
    path("auth/logout/", LogoutAPIView.as_view(), name="logout"),
]