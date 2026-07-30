from rest_framework.routers import DefaultRouter

from .views import (
    ClubViewSet,
    ClubMembershipViewSet,
)


router = DefaultRouter()

router.register(
    r"clubs",
    ClubViewSet,
    basename="clubs",
)

router.register(
    r"club-memberships",
    ClubMembershipViewSet,
    basename="club-memberships",
)


urlpatterns = router.urls