from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        LECTURER = "LECTURER", "Lecturer"
        ADMIN = "ADMIN", "Admin"

    # core identity
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    # profile layer
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    # enterprise security fields
    is_verified = models.BooleanField(
        default=False,
    )

    failed_login_attempts = models.IntegerField(
        default=0,
    )

    locked_until = models.DateTimeField(
        null=True,
        blank=True,
    )

    # audit
    last_login_ip = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.username} ({self.role})"