from rest_framework.permissions import BasePermission


class IsAuthenticatedUser(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
        )


class IsStudent(BasePermission):
    """
    Allows students only.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "STUDENT"
        )


class IsLecturer(BasePermission):
    """
    Allows lecturers only.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "LECTURER"
        )


class IsAdmin(BasePermission):
    """
    System administrators.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "ADMIN"
        )


class IsOrganizationExecutive(BasePermission):
    """
    Allows users who hold executive positions
    inside an organization.

    Example:
    - COMSOC President
    - MPR Secretary
    - Projects Team Lead
    """

    EXECUTIVE_ROLES = [
        "TEAM_LEAD",
        "SECRETARY",
        "TREASURER",
        "VICE_PRESIDENT",
        "PRESIDENT",
        "CHAIRPERSON",
        "EXECUTIVE",
    ]

    def has_permission(self, request, view):

        if not (
            request.user
            and request.user.is_authenticated
        ):
            return False

        return request.user.organization_memberships.filter(
            role__in=self.EXECUTIVE_ROLES,
            status="ACTIVE",
        ).exists()