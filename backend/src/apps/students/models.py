from django.conf import settings
from django.db import models


class StudentProfile(models.Model):
    """
    Stores student-specific information.

    Authentication and authorization remain on the User model.
    """

    YEAR_CHOICES = [
        (1, "Year 1"),
        (2, "Year 2"),
        (3, "Year 3"),
        (4, "Year 4"),
        (5, "Year 5"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )

    student_id = models.CharField(
        max_length=30,
        unique=True,
    )

    programme = models.CharField(
        max_length=100,
    )

    faculty = models.CharField(
        max_length=100,
    )

    year_of_study = models.PositiveSmallIntegerField(
        choices=YEAR_CHOICES,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["student_id"]
        verbose_name = "Student Profile"
        verbose_name_plural = "Student Profiles"

    def __str__(self):
        return f"{self.student_id} - {self.user.username}" 