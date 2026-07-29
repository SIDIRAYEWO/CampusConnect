from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):

    organizer_username = serializers.CharField(
        source="organizer.username",
        read_only=True,
    )

    class Meta:
        model = Event

        fields = [
            "id",
            "organizer",
            "organizer_username",
            "title",
            "description",
            "event_type",
            "audience",
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
            "published_at",
            "created_at",
            "updated_at",
        ]