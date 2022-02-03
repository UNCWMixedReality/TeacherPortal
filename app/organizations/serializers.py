from rest_framework import serializers
from users.models import Staff
from users.serializers import StaffSerializer

from .models import Course, Group, Headset, Organization, Student


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("name", "address")


class CourseSerializer(serializers.ModelSerializer):
    org_id = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    staff_id = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all())

    class Meta:
        model = Course
        fields = ("name", "staff_id", "org_id")
