from rest_framework import routers

from apps.cars.views import CarAPIViewSet, SpecialMarksAPIViewSet, PeriodsOwnershipAPIViewSet, CarPostAPIViewSet

router = routers.DefaultRouter()
router.register('cars', CarAPIViewSet, "api_cars")
router.register('special', SpecialMarksAPIViewSet, "api_special_marks")
router.register('periods', PeriodsOwnershipAPIViewSet, "api_periods_ownership")
router.register('posts', CarPostAPIViewSet, "api_posts")

urlpatterns = router.urls