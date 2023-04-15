from django.db import models


class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    tmdb_id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=255)


class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    tmdb_id = models.BigIntegerField(null=True)
    title = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=15)
    release_date = models.DateField()
    runtime = models.IntegerField(null=True)
    cinebase_rating = models.FloatField()
    poster_path = models.CharField(max_length=255, null=True)
    overview = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField(Genre)

    class Meta:
        ordering = ["created"]
