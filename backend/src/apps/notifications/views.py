from rest_framework import filters, viewsets

from apps.accounts.permissions import IsAdmin

from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    """
    CRUD API for user notifications.

    Currently restricted to administrators.
    """

    queryset = (
        Notification.objects
        .select_related(
            "recipient",
            "organization",
        )
        .all()
    )

    serializer_class = NotificationSerializer

    permission_classes = [
        IsAdmin,
    ]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "title",
        "message",
        "recipient__username",
        "organization__name",
    ]

    ordering_fields = [
        "created_at",
        "notification_type",
        "is_read",
    ]

    ordering = [
        "-created_at",
    ]