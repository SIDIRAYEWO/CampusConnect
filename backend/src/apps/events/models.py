from django.conf import settings
from django.db import models

from apps.organizations.models import Organization


class Event(models.Model):
    """
    University events created by administrators and organization leaders.
    """

    class EventType(models.TextChoices):
        ACADEMIC = "ACADEMIC", "Academic"
        SOCIAL = "SOCIAL", "Social"
        SPORTS = "SPORTS", "Sports"
        WORKSHOP = "WORKSHOP", "Workshop"
        SEMINAR = "SEMINAR", "Seminar"
        CONFERENCE = "CONFERENCE", "Conference"
        OTHER = "OTHER", "Other"

    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PUBLISHED = "PUBLISHED", "Published"
        CANCELLED = "CANCELLED", "Cancelled"
        COMPLETED = "COMPLETED", "Completed"

    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="events",
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="events",
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField()

    event_type = models.CharField(
        max_length=20,
        choices=EventType.choices,
        default=EventType.OTHER,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    venue = models.CharField(
        max_length=200,
    )

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["start_time"]
        verbose_name = "Event"
        verbose_name_plural = "Events"

        indexes = [
            models.Index(fields=["organization"]),
            models.Index(fields=["event_type"]),
            models.Index(fields=["status"]),
            models.Index(fields=["start_time"]),
        ]

    def __str__(self):
        return self.title