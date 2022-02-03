# users/serializers.py
from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("email", "username", "name")


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = ("user", "organization")
