from django.conf import settings
from django.db import models

from apps.core.models import (
    UUIDModel,
    TimestampedModel,
)

from apps.organizations.models import Organization


class Notification(
    UUIDModel,
    TimestampedModel,
):
    """
    Represents a notification sent to a user.
    """

    class NotificationType(models.TextChoices):
        ANNOUNCEMENT = "ANNOUNCEMENT", "Announcement"
        EVENT = "EVENT", "Event"
        ORGANIZATION = "ORGANIZATION", "Organization"
        SYSTEM = "SYSTEM", "System"
        SECURITY = "SECURITY", "Security"

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="notifications",
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=200,
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=20,
        choices=NotificationType.choices,
        default=NotificationType.SYSTEM,
    )

    is_read = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f"{self.recipient.username} - {self.title}"