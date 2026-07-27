from django.test import TestCase

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from apps.students.models import StudentProfile


User = get_user_model()


class StudentProfileAPITestCase(APITestCase):

    def setUp(self):
        # Create admin user
        self.admin = User.objects.create_user(
            username="test_admin",
            email="admin@test.com",
            password="Admin@123",
            role="ADMIN",
        )

        # Create student user
        self.student = User.objects.create_user(
            username="test_student",
            email="student@test.com",
            password="Student@123",
            role="STUDENT",
        )

        # Create student profile
        self.profile = StudentProfile.objects.create(
            user=self.student,
            student_id="BSC-CS-TEST-001",
            programme="BSc Computer Science",
            faculty="Science",
            year_of_study=3,
        )

        self.url = "/api/v1/students/"


    def test_admin_can_view_students(self):
        """
        Admin users should be able to access student profiles.
        """

        self.client.force_authenticate(
            user=self.admin
        )

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_student_cannot_view_all_students(self):
        """
        Students should not access admin-only endpoints.
        """

        self.client.force_authenticate(
            user=self.student
        )

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )


    def test_unauthenticated_user_cannot_view_students(self):
        """
        Anonymous users should be rejected.
        """

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )


    def test_student_profile_created(self):
        """
        StudentProfile should correctly link to User.
        """

        self.assertEqual(
            self.profile.user,
            self.student
        )

        self.assertEqual(
            self.profile.student_id,
            "BSC-CS-TEST-001"
        )
