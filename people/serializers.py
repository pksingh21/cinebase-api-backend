from rest_framework import serializers
from people.models import Person, MovieCredit


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class MovieCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCredit
        fields = "__all__"
