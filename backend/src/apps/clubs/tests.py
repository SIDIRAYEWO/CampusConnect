from django.test import TestCase

from apps.accounts.models import User

from .models import (
    Club,
    ClubMembership,
)


class ClubModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="club_admin",
            password="Admin@123",
            role="ADMIN",
            email="admin@test.com",
        )

        self.club = Club.objects.create(
            name="Computer Science Society",
            description="Official Computer Science club.",
            category="TECHNOLOGY",
            email="css@test.com",
            advisor_name="Dr. Banda",
            is_verified=True,
        )


    def test_create_club(self):
        self.assertEqual(
            self.club.name,
            "Computer Science Society",
        )

        self.assertEqual(
            self.club.category,
            "TECHNOLOGY",
        )


    def test_create_membership(self):
        membership = ClubMembership.objects.create(
            user=self.user,
            club=self.club,
            role=ClubMembership.Role.MEMBER,
            status=ClubMembership.Status.ACTIVE,
        )

        self.assertEqual(
            membership.user,
            self.user,
        )

        self.assertEqual(
            membership.club,
            self.club,
        )

        self.assertEqual(
            membership.status,
            ClubMembership.Status.ACTIVE,
        )


    def test_membership_status_choices(self):
        valid_statuses = [
            ClubMembership.Status.PENDING,
            ClubMembership.Status.ACTIVE,
            ClubMembership.Status.REJECTED,
        ]

        for status in valid_statuses:
            membership = ClubMembership(
                user=self.user,
                club=self.club,
                role=ClubMembership.Role.MEMBER,
                status=status,
            )

            self.assertIn(
                membership.status,
                valid_statuses,
            )