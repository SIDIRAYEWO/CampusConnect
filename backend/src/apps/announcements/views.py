from django.utils import timezone

from rest_framework import filters, viewsets

from apps.accounts.permissions import IsAdmin

from .models import Announcement
from .serializers import AnnouncementSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    """
    CRUD API for organization announcements.

    Currently restricted to administrators.
    """

    queryset = (
        Announcement.objects
        .select_related(
            "author",
            "organization",
        )
        .all()
    )

    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdmin]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "title",
        "content",
        "author__username",
        "organization__name",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
        "published_at",
        "priority",
    ]

    ordering = [
        "-created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            published_at=(
                timezone.now()
                if serializer.validated_data.get("status")
                == Announcement.Status.PUBLISHED
                else None
            ),
        )