from rest_framework import status
from rest_framework.test import APITestCase

from apps.accounts.models import User
from apps.organizations.models import Organization

from .models import Announcement


class AnnouncementModelTest(APITestCase):

    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin_test",
            password="Admin@123",
            role="ADMIN",
            email="admin@test.com",
        )

        self.organization = Organization.objects.create(
            name="Computer Science Society",
            description="Official Computer Science Society",
            organization_type=Organization.OrganizationType.SOCIETY,
            is_verified=True,
        )

    def test_create_announcement(self):
        announcement = Announcement.objects.create(
            author=self.admin,
            organization=self.organization,
            title="Semester Opens",
            content="Semester begins next Monday.",
        )

        self.assertEqual(
            announcement.title,
            "Semester Opens",
        )

        self.assertEqual(
            announcement.author,
            self.admin,
        )

        self.assertEqual(
            announcement.organization,
            self.organization,
        )


class AnnouncementAPITest(APITestCase):

    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin_api",
            password="Admin@123",
            role="ADMIN",
            email="admin_api@test.com",
        )

        self.student = User.objects.create_user(
            username="student_api",
            password="Student@123",
            role="STUDENT",
            email="student_api@test.com",
        )

        self.organization = Organization.objects.create(
            name="Students Representative Council",
            description="SRC",
            organization_type=Organization.OrganizationType.SRC,
            is_verified=True,
        )

        self.url = "/api/v1/announcements/"

    def authenticate(self, user):
        self.client.force_authenticate(user=user)

    def test_admin_can_create_announcement(self):
        self.authenticate(self.admin)

        response = self.client.post(
            self.url,
            {
                "organization": str(self.organization.id),
                "title": "Registration Opens",
                "content": "Registration starts next week.",
                "priority": "HIGH",
                "status": "PUBLISHED",
            },
            format="json",
        )

       

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        announcement = Announcement.objects.first()

        self.assertEqual(
            announcement.author,
            self.admin,
        )

        self.assertEqual(
            announcement.organization,
            self.organization,
        )

        self.assertIsNotNone(
            announcement.published_at,
        )

    def test_student_cannot_create_announcement(self):
        self.authenticate(self.student)

        response = self.client.post(
            self.url,
            {
                "organization": str(self.organization.id),
                "title": "Fake Announcement",
                "content": "Students should not publish this.",
                "priority": "NORMAL",
                "status": "PUBLISHED",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_unauthenticated_user_cannot_access(self):
        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )