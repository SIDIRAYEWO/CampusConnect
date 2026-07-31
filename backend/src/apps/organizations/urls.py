from rest_framework.routers import DefaultRouter

from .views import (
    OrganizationViewSet,
    OrganizationMembershipViewSet,
)


router = DefaultRouter()


router.register(
    r"organizations",
    OrganizationViewSet,
    basename="organizations",
)


router.register(
    r"organization-memberships",
    OrganizationMembershipViewSet,
    basename="organization-memberships",
)


urlpatterns = router.urls