# users/serializers.py
from organizations.models import Organization
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

    def create(self, validated_data):
        user = self.context["request"].user

        if user.is_superuser:
            if isinstance(validated_data["organization"], int):
                organization = Organization.objects.get(
                    id=validated_data["organization"]
                )
                staff = models.Staff.objects.create(
                    user=validated_data["user"], organization=organization
                )
                staff.save()
                return staff
            else:
                staff = models.Staff.objects.create(**validated_data)
                staff.save()
                return staff
        else:
            requesting_staff = models.Staff.objects.get(user=user)
            organization = Organization.objects.get(id=requesting_staff.organization)
            staff = models.Staff.objects.create(
                user=validated_data["user"], organization=organization
            )
            staff.save()
            return staff

    def to_representation(self, instance):
        return {
            "user": {
                "id": instance.user.id,
                "name": instance.user.name,
                "email": instance.user.email,
            },
            "organization": {
                "id": instance.organization.id,
                "name": instance.organization.name,
                "address": instance.organization.address,
            },
        }
