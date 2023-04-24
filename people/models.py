from django.db import models
from django.utils.translation import gettext_lazy as _
from movies.models import Movie


class Person(models.Model):
    class Gender(models.IntegerChoices):
        NOT_KNOWN = 0, _("Not known")
        MALE = 1, _("Male")
        FEMALE = 2, _("Female")
        NOT_APPLICABLE = 9, _("Not applicable")

    id = models.BigAutoField(primary_key=True)
    tmdb_id = models.BigIntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    gender = models.IntegerField(choices=Gender.choices, default=Gender.NOT_KNOWN)
    birthday = models.DateField(null=True, blank=True)
    deathday = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "people_person"


class MovieCredit(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    credits_type = models.CharField(max_length=255)
