from rest_framework import serializers

from .models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
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
            "title",
            "content",
            "audience",
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
            "created_at",
            "updated_at",
            "deleted_at",
        ]