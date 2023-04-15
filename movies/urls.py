from movies.views import GenreViewSet, MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"movies", MovieViewSet, basename="movie")
urlpatterns = router.urls
