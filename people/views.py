from rest_framework import viewsets
from people.models import Person, MovieCredit
from people.serializers import PersonSerializer, MovieCreditSerializer
from profiles.permissions import IsDataEntryistOrReadOnly
from django_filters import rest_framework as filters


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsDataEntryistOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["name"]


class MovieCreditViewSet(viewsets.ModelViewSet):
    queryset = MovieCredit.objects.all()
    serializer_class = MovieCreditSerializer
    permission_classes = [IsDataEntryistOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["person", "movie", "credits_type"]
