from rest_framework import serializers

from .models import (
    Club,
    ClubMembership,
)


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club

        fields = [
            "id",
            "name",
            "description",
            "category",
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
            "created_at",
            "updated_at",
            "deleted_at",
        ]


class ClubMembershipSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True,
    )

    club_name = serializers.CharField(
        source="club.name",
        read_only=True,
    )

    class Meta:
        model = ClubMembership

        fields = [
            "id",
            "user",
            "username",
            "club",
            "club_name",
            "role",
            "status",
            "joined_at",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "username",
            "club_name",
            "joined_at",
            "created_at",
            "updated_at",
        ]