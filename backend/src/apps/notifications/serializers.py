from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    recipient_username = serializers.CharField(
        source="recipient.username",
        read_only=True,
    )

    class Meta:
        model = Notification

        fields = [
            "id",
            "recipient",
            "recipient_username",
            "title",
            "message",
            "notification_type",
            "is_read",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "recipient_username",
            "created_at",
            "updated_at",
        ]