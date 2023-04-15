from rest_framework import serializers
from user_reviews.models import UserReview


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = "__all__"
