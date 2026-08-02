from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    recipient_username = serializers.CharField(
        source="recipient.username",
        read_only=True,
    )

    organization_name = serializers.CharField(
        source="organization.name",
        read_only=True,
    )

    class Meta:
        model = Notification

        fields = [
            "id",
            "recipient",
            "recipient_username",
            "organization",
            "organization_name",
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
            "organization_name",
            "created_at",
            "updated_at",
        ]