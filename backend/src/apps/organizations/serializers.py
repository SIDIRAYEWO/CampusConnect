from rest_framework import serializers

from .models import (
    Organization,
    OrganizationMembership,
)


class OrganizationSerializer(serializers.ModelSerializer):

    parent_name = serializers.CharField(
        source="parent.name",
        read_only=True,
    )

    registered_with_name = serializers.CharField(
        source="registered_with.name",
        read_only=True,
    )

    class Meta:
        model = Organization

        fields = [
            "id",
            "name",
            "description",
            "organization_type",
            "parent",
            "parent_name",
            "registered_with",
            "registered_with_name",
            "logo",
            "email",
            "advisor_name",
            "is_verified",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

        read_only_fields = [
            "id",
            "parent_name",
            "registered_with_name",
            "created_at",
            "updated_at",
            "deleted_at",
        ]


class OrganizationMembershipSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True,
    )

    organization_name = serializers.CharField(
        source="organization.name",
        read_only=True,
    )

    class Meta:
        model = OrganizationMembership

        fields = [
            "id",
            "user",
            "username",
            "organization",
            "organization_name",
            "role",
            "status",
            "joined_at",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "username",
            "organization_name",
            "joined_at",
            "created_at",
            "updated_at",
        ]