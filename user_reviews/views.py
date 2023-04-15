from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from user_reviews.models import UserReview
from user_reviews.serializers import UserReviewSerializer


class UserReviewViewSet(viewsets.ModelViewSet):
    serializer_class = UserReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "movie"]

    def get_queryset(self):
        if self.request.method in SAFE_METHODS:
            return UserReview.objects.all()
        return UserReview.objects.filter(user=self.request.user)
