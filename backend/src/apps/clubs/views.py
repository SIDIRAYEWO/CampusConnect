from rest_framework import filters, viewsets

from apps.accounts.permissions import IsAdmin

from .models import (
    Club,
    ClubMembership,
)

from .serializers import (
    ClubSerializer,
    ClubMembershipSerializer,
)


class ClubViewSet(viewsets.ModelViewSet):
    """
    CRUD API for university clubs.

    Currently restricted to administrators.
    """

    queryset = (
        Club.objects
        .all()
    )

    serializer_class = ClubSerializer
    permission_classes = [IsAdmin]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "name",
        "description",
        "advisor_name",
    ]

    ordering_fields = [
        "name",
        "created_at",
    ]

    ordering = [
        "name",
    ]


class ClubMembershipViewSet(viewsets.ModelViewSet):
    """
    CRUD API for club memberships.

    Handles users joining and being assigned roles within clubs.
    """

    queryset = (
        ClubMembership.objects
        .select_related(
            "user",
            "club",
        )
        .all()
    )

    serializer_class = ClubMembershipSerializer
    permission_classes = [IsAdmin]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "user__username",
        "club__name",
    ]

    ordering_fields = [
        "joined_at",
        "role",
        "status",
    ]

    ordering = [
        "-joined_at",
    ]