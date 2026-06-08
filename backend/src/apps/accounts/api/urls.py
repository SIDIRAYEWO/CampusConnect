# apps/accounts/api/urls.py

from django.urls import path
from .views import UserListCreateAPIView

urlpatterns = [
    path("users/", UserListCreateAPIView.as_view(), name="users"),
]