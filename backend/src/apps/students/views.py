from rest_framework import viewsets

from .models import StudentProfile
from .serializers import StudentProfileSerializer

from apps.accounts.permissions import IsAdmin


class StudentProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing student profiles.

    Currently restricted to administrators.
    Student self-service access will be added
    with advanced RBAC.
    """

    queryset = StudentProfile.objects.select_related(
        "user"
    ).all()

    serializer_class = StudentProfileSerializer

    permission_classes = [
        IsAdmin,
    ]