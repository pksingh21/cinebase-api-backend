from django.contrib.auth import get_user_model
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        USER_MODEL = get_user_model()
        model = USER_MODEL
        fields = ["pk", USER_MODEL.USERNAME_FIELD, "first_name", "last_name"]
