from django.conf import settings
from django.db import models


class Event(models.Model):
    """
    University events created by administrators and approved organizers.
    """

    class EventType(models.TextChoices):
        ACADEMIC = "ACADEMIC", "Academic"
        SOCIAL = "SOCIAL", "Social"
        SPORTS = "SPORTS", "Sports"
        CLUB = "CLUB", "Club"
        OTHER = "OTHER", "Other"

    class Audience(models.TextChoices):
        ALL = "ALL", "All Students"
        FACULTY = "FACULTY", "Faculty"
        DEPARTMENT = "DEPARTMENT", "Department"
        CLUB = "CLUB", "Club"

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

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField()

    event_type = models.CharField(
        max_length=20,
        choices=EventType.choices,
        default=EventType.OTHER,
    )

    audience = models.CharField(
        max_length=20,
        choices=Audience.choices,
        default=Audience.ALL,
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

    def __str__(self):
        return self.title