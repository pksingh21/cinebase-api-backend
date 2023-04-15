from django.db import models
from django.conf import settings
from movies.models import Movie


class UserReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField(null=True, blank=True)
