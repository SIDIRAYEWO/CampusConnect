from django.conf import settings
from django.db import models

from apps.core.models import (
    UUIDModel,
    TimestampedModel,
    SoftDeleteModel,
)

from apps.organizations.models import Organization


class Announcement(
    UUIDModel,
    TimestampedModel,
    SoftDeleteModel,
):
    """
    University announcements published by organizations.
    """

    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        NORMAL = "NORMAL", "Normal"
        HIGH = "HIGH", "High"
        URGENT = "URGENT", "Urgent"

    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PUBLISHED = "PUBLISHED", "Published"
        ARCHIVED = "ARCHIVED", "Archived"

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="announcements",
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="announcements",
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=200,
    )

    content = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.NORMAL,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"

        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["organization"]),
            models.Index(fields=["priority"]),
            models.Index(fields=["published_at"]),
        ]

    def __str__(self):
        return self.title