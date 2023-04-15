from rest_framework import viewsets
from movies.models import Genre, Movie
from movies.serializers import GenreSerializer, MovieSerializer
from profiles.permissions import IsDataEntryistOrReadOnly
from django_filters import rest_framework as filters


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsDataEntryistOrReadOnly]


class MovieFilter(filters.FilterSet):
    released_after = filters.DateFilter(field_name="release_date", lookup_expr="gte")
    released_before = filters.DateFilter(field_name="release_date", lookup_expr="lte")

    class Meta:
        model = Movie
        fields = ["title", "language"]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsDataEntryistOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = MovieFilter
