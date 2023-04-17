from rest_framework import routers

from apps.cars.views import CarAPIViewSet, SpecialMarksAPIViewSet, PeriodsOwnershipAPIViewSet, CarPostAPIViewSet, CarPostImageAPIViewSet, CarPostCommentAPIViewSet, CarPostFavoriteAPIViewSet

router = routers.DefaultRouter()
router.register('cars', CarAPIViewSet, "api_cars")
router.register('special', SpecialMarksAPIViewSet, "api_special_marks")
router.register('periods', PeriodsOwnershipAPIViewSet, "api_periods_ownership")
router.register('posts', CarPostAPIViewSet, "api_posts")
router.register('image', CarPostImageAPIViewSet, "api_posts_image")
router.register('comment', CarPostCommentAPIViewSet, "api_posts_comment")
router.register('favorite', CarPostFavoriteAPIViewSet, "api_posts_favotite")

urlpatterns = router.urls