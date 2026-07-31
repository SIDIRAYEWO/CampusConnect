from django.test import TestCase

from apps.accounts.models import User

from .models import (
    Organization,
    OrganizationMembership,
)


class OrganizationModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="yewo10",
            password="Password@123",
            email="yewo@test.com",
            role="ADMIN",
        )

        self.src = Organization.objects.create(
            name="Students Representative Council",
            description="UNIMA student governing body.",
            organization_type="SRC",
            email="src@test.com",
            is_verified=True,
        )

        self.department = Organization.objects.create(
            name="Computer Science Department",
            description="Computer Science academic department.",
            organization_type="DEPARTMENT",
            email="cs@test.com",
            is_verified=True,
        )


        self.society = Organization.objects.create(
            name="Computer Science Society",
            description="CS student society.",
            organization_type="SOCIETY",
            parent=self.department,
            registered_with=self.src,
            email="comsoc@test.com",
            is_verified=True,
        )


    def test_society_has_department_parent(self):

        self.assertEqual(
            self.society.parent,
            self.department,
        )


    def test_society_registered_with_src(self):

        self.assertEqual(
            self.society.registered_with,
            self.src,
        )


    def test_create_membership(self):

        membership = OrganizationMembership.objects.create(
            user=self.user,
            organization=self.society,
            role="MEMBER",
            status="ACTIVE",
        )

        self.assertEqual(
            membership.organization,
            self.society,
        )

        self.assertEqual(
            membership.status,
            "ACTIVE",
        )