from rest_framework.routers import DefaultRouter
from user_reviews.views import UserReviewViewSet

router = DefaultRouter()
router.register(r"reviews", UserReviewViewSet, basename="review")
urlpatterns = router.urls
