from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import Staff
from users.serializers import StaffSerializer

from .models import Course, Group, Headset, Organization, Student


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("name", "address")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("name", "staff_id", "org_id")

    def create(self, validated_data):
        user = self.context["request"].user

        if user.is_superuser:
            print("Hi! I'm a superuser")
            print(user)
            print(validated_data)
            if isinstance(validated_data["org_id"], int):
                organization = Organization.objects.get(id=validated_data["org_id"])
                course = Course.objects.create(
                    name=validated_data["name"],
                    org_id=organization,
                    staff_id=validated_data["staff_id"],
                )
                course.save()
                return course
            else:
                course = Course.objects.create(**validated_data)
                course.save()
                return course
        else:
            requesting_staff = Staff.objects.get(user=user)
            organization = Organization.objects.get(id=requesting_staff.organization)
            course = Course.objects.create(
                name=validated_data["name"],
                org_id=organization,
                staff_id=requesting_staff,
            )
            course.save()
            return course

    def validate(self, attrs):
        user = self.context["request"].user

        if not user.is_superuser:
            if user.id != attrs.staff_id:
                raise ValidationError(
                    detail={
                        "detail": "Non admin users can only create courses for themselves"
                    }
                )

            staff = Staff.objects.get(user=user)
            if staff.organization.id != attrs.org_id:
                raise ValidationError(
                    detail={
                        "detail": "Non admin users can only create courses within their own organization"
                    }
                )

        super().validate(attrs)
        return attrs


class HeadsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headset
        fields = ("org_id", "mac_address")
