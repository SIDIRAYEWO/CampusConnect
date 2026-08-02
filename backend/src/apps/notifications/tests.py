from django.test import TestCase

from apps.accounts.models import User
from apps.organizations.models import Organization

from .models import Notification


class NotificationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="notification_user",
            password="Test@123",
            role="STUDENT",
            email="student@test.com",
        )

        self.organization = Organization.objects.create(
            name="Computer Science Society",
            description="Official CS student organization.",
            organization_type=Organization.OrganizationType.SOCIETY,
            is_verified=True,
        )


    def test_create_system_notification(self):

        notification = Notification.objects.create(
            recipient=self.user,
            title="Welcome Notification",
            message="Welcome to CampusConnect.",
            notification_type=Notification.NotificationType.SYSTEM,
            is_read=False,
        )

        self.assertEqual(
            notification.recipient,
            self.user,
        )

        self.assertEqual(
            notification.title,
            "Welcome Notification",
        )

        self.assertFalse(
            notification.is_read,
        )


    def test_create_organization_notification(self):

        notification = Notification.objects.create(
            recipient=self.user,
            organization=self.organization,
            title="New Organization Announcement",
            message="Computer Science Society posted a new update.",
            notification_type=Notification.NotificationType.ANNOUNCEMENT,
        )

        self.assertEqual(
            notification.organization,
            self.organization,
        )

        self.assertEqual(
            notification.notification_type,
            Notification.NotificationType.ANNOUNCEMENT,
        )


    def test_mark_notification_as_read(self):

        notification = Notification.objects.create(
            recipient=self.user,
            title="Announcement Posted",
            message="A new announcement has been posted.",
            notification_type=Notification.NotificationType.ANNOUNCEMENT,
        )

        notification.is_read = True
        notification.save()

        notification.refresh_from_db()

        self.assertTrue(
            notification.is_read,
        )