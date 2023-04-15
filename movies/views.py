from rest_framework import viewsets
from movies.models import Genre, Movie
from movies.serializers import GenreSerializer, MovieSerializer
from profiles.permissions import IsDataEntryistOrReadOnly


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsDataEntryistOrReadOnly]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsDataEntryistOrReadOnly]
