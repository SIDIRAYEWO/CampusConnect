from rest_framework import filters, viewsets

from apps.accounts.permissions import IsAdmin

from .models import (
    Organization,
    OrganizationMembership,
)

from .serializers import (
    OrganizationSerializer,
    OrganizationMembershipSerializer,
)


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    CRUD API for university organizations.
    """

    queryset = Organization.objects.all()

    serializer_class = OrganizationSerializer

    permission_classes = [
        IsAdmin,
    ]

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


class OrganizationMembershipViewSet(viewsets.ModelViewSet):
    """
    CRUD API for organization memberships.
    """

    queryset = OrganizationMembership.objects.all()

    serializer_class = OrganizationMembershipSerializer

    permission_classes = [
        IsAdmin,
    ]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "user__username",
        "organization__name",
        "role",
    ]

    ordering_fields = [
        "joined_at",
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]