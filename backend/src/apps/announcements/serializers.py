from rest_framework import serializers

from .models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):

    organization_name = serializers.CharField(
        source="organization.name",
        read_only=True,
    )

    author_username = serializers.CharField(
        source="author.username",
        read_only=True,
    )

    class Meta:
        model = Announcement

        fields = [
            "id",
            "author",
            "author_username",
            "organization",
            "organization_name",
            "title",
            "content",
            "priority",
            "status",
            "published_at",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

        read_only_fields = [
            "id",
            "author",
            "author_username",
            "organization_name",
            "created_at",
            "updated_at",
            "deleted_at",
        ]