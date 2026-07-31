from django.conf import settings
from django.db import models

from apps.core.models import (
    UUIDModel,
    TimestampedModel,
    SoftDeleteModel,
)


class Organization(
    UUIDModel,
    TimestampedModel,
    SoftDeleteModel,
):
    """
    Represents a university organization.
    """

    class OrganizationType(models.TextChoices):
        UNIVERSITY = "UNIVERSITY", "University"
        SRC = "SRC", "SRC"
        FACULTY = "FACULTY", "Faculty"
        DEPARTMENT = "DEPARTMENT", "Department"
        SOCIETY = "SOCIETY", "Society"
        TEAM = "TEAM", "Team"
        CLUB = "CLUB", "Club"
        COMMITTEE = "COMMITTEE", "Committee"
        ASSOCIATION = "ASSOCIATION", "Association"
        OTHER = "OTHER", "Other"

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    organization_type = models.CharField(
        max_length=30,
        choices=OrganizationType.choices,
        default=OrganizationType.OTHER,
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="children",
        null=True,
        blank=True,
    )

    registered_with = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="registered_organizations",
        null=True,
        blank=True,
    )

    logo = models.ImageField(
        upload_to="organizations/",
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
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name


class OrganizationMembership(
    UUIDModel,
    TimestampedModel,
):
    """
    Represents a user's membership in an organization.
    """

    class Role(models.TextChoices):
        MEMBER = "MEMBER", "Member"
        TEAM_LEAD = "TEAM_LEAD", "Team Lead"
        SECRETARY = "SECRETARY", "Secretary"
        TREASURER = "TREASURER", "Treasurer"
        VICE_PRESIDENT = "VICE_PRESIDENT", "Vice President"
        PRESIDENT = "PRESIDENT", "President"
        CHAIRPERSON = "CHAIRPERSON", "Chairperson"
        EXECUTIVE = "EXECUTIVE", "Executive"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"
        ALUMNI = "ALUMNI", "Alumni"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="organization_memberships",
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="memberships",
    )

    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.MEMBER,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    joined_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["organization", "user"]
        verbose_name = "Organization Membership"
        verbose_name_plural = "Organization Memberships"

        constraints = [
            models.UniqueConstraint(
                fields=["user", "organization"],
                name="unique_user_organization_membership",
            )
        ]

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.organization.name} "
            f"({self.role})"
        )