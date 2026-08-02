from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):

    organizer_username = serializers.CharField(
        source="organizer.username",
        read_only=True,
    )

    organization_name = serializers.CharField(
        source="organization.name",
        read_only=True,
    )

    class Meta:
        model = Event

        fields = [
            "id",
            "organizer",
            "organizer_username",
            "organization",
            "organization_name",
            "title",
            "description",
            "event_type",
            "status",
            "venue",
            "start_time",
            "end_time",
            "published_at",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "organizer",
            "organizer_username",
            "organization_name",
            "published_at",
            "created_at",
            "updated_at",
        ]