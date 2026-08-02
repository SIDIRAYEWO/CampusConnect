from django.utils import timezone

from rest_framework import filters, viewsets

from apps.accounts.permissions import IsAdmin

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    CRUD API for university events.

    Currently restricted to administrators.
    """

    queryset = (
        Event.objects
        .select_related(
            "organizer",
            "organization",
        )
        .all()
    )

    serializer_class = EventSerializer

    permission_classes = [
        IsAdmin,
    ]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "title",
        "description",
        "venue",
        "organizer__username",
        "organization__name",
    ]

    ordering_fields = [
        "start_time",
        "end_time",
        "created_at",
        "updated_at",
        "event_type",
    ]

    ordering = [
        "start_time",
    ]

    def perform_create(self, serializer):
        serializer.save(
            organizer=self.request.user,
            published_at=(
                timezone.now()
                if serializer.validated_data.get("status") == Event.Status.PUBLISHED
                else None
            ),
        )