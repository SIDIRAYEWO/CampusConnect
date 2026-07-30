from django.test import TestCase

from apps.accounts.models import User

from .models import Notification


class NotificationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="notification_user",
            password="Test@123",
            role="STUDENT",
            email="student@test.com",
        )


    def test_create_notification(self):
        notification = Notification.objects.create(
            recipient=self.user,
            title="Welcome Notification",
            message="Welcome to CampusConnect.",
            notification_type="SYSTEM",
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


    def test_mark_notification_as_read(self):
        notification = Notification.objects.create(
            recipient=self.user,
            title="Announcement Posted",
            message="A new announcement has been posted.",
            notification_type="ANNOUNCEMENT",
        )

        notification.is_read = True
        notification.save()

        notification.refresh_from_db()

        self.assertTrue(
            notification.is_read,
        )