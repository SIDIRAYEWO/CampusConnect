from django.test import TestCase

from apps.accounts.models import User

from .models import Event


class EventModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="event_admin",
            password="Admin@123",
            role="ADMIN",
            email="event_admin@test.com",
        )

    def test_create_event(self):
        event = Event.objects.create(
            organizer=self.user,
            title="Career Fair",
            description="A university career networking event.",
            event_type="ACADEMIC",
            audience="ALL",
            status="PUBLISHED",
            venue="Main Hall",
            start_time="2026-08-10T09:00:00Z",
            end_time="2026-08-10T15:00:00Z",
        )

        self.assertEqual(
            event.title,
            "Career Fair",
        )

        self.assertEqual(
            event.organizer,
            self.user,
        )

    def test_event_default_status(self):
        event = Event.objects.create(
            organizer=self.user,
            title="Club Meeting",
            description="Monthly club meeting.",
            venue="Room 101",
            start_time="2026-08-15T10:00:00Z",
            end_time="2026-08-15T12:00:00Z",
        )

        self.assertEqual(
            event.status,
            Event.Status.DRAFT,
        )