from people.views import PersonViewSet, MovieCreditViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"people", PersonViewSet, basename="person")
router.register(r"credits", MovieCreditViewSet, basename="credit")
urlpatterns = router.urls
