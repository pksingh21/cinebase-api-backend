from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from profiles.serializers import ProfileSerializer


class ProfileList(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]
