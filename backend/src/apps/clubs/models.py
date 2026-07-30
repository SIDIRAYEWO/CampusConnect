from django.conf import settings
from django.db import models

from apps.core.models import (
    UUIDModel,
    TimestampedModel,
    SoftDeleteModel,
)


class Club(
    UUIDModel,
    TimestampedModel,
    SoftDeleteModel,
):
    """
    Official university club.
    """

    class Category(models.TextChoices):
        ACADEMIC = "ACADEMIC", "Academic"
        SPORTS = "SPORTS", "Sports"
        CULTURAL = "CULTURAL", "Cultural"
        RELIGIOUS = "RELIGIOUS", "Religious"
        TECHNOLOGY = "TECHNOLOGY", "Technology"
        OTHER = "OTHER", "Other"

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    description = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER,
    )

    logo = models.ImageField(
        upload_to="clubs/",
        blank=True,
        null=True,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    advisor_name = models.CharField(
        max_length=150,
        blank=True,
    )

    is_verified = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Club"
        verbose_name_plural = "Clubs"

    def __str__(self):
        return self.name


class ClubMembership(
    UUIDModel,
    TimestampedModel,
):
    """
    Represents a user's membership in a university club.
    """

    class Role(models.TextChoices):
        MEMBER = "MEMBER", "Member"
        SECRETARY = "SECRETARY", "Secretary"
        TREASURER = "TREASURER", "Treasurer"
        VICE_PRESIDENT = "VICE_PRESIDENT", "Vice President"
        PRESIDENT = "PRESIDENT", "President"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACTIVE = "ACTIVE", "Active"
        REJECTED = "REJECTED", "Rejected"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="club_memberships",
    )

    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name="memberships",
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.MEMBER,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    joined_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["club", "user"]
        verbose_name = "Club Membership"
        verbose_name_plural = "Club Memberships"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "club"],
                name="unique_user_club_membership",
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.club.name} ({self.role})"