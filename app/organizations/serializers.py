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

    def create(self, validated_data):
        user = self.context["request"].user

        if user.is_superuser:
            if isinstance(validated_data["org_id"], int):
                organization = Organization.objects.get(id=validated_data["org_id"])
                headset = Headset.objects.create(
                    org_id=organization,
                    mac_address=validated_data["mac_address"],
                )
                headset.save()
                return headset
            else:
                headset = Headset.objects.create(**validated_data)
                headset.save()
                return headset
        else:
            requesting_staff = Staff.objects.get(user=user)
            organization = Organization.objects.get(id=requesting_staff.organization)
            headset = Headset.objects.create(
                org_id=organization, mac_address=validated_data["mac_address"]
            )
            headset.save()
            return headset

    def validate(self, attrs):
        user = self.context["request"].user

        if not user.is_superuser:
            if user.id != attrs.staff_id:
                raise ValidationError(
                    detail={
                        "detail": "Non admin users can only create headsets for themselves"
                    }
                )

            staff = Staff.objects.get(user=user)
            if staff.organization.id != attrs.org_id:
                raise ValidationError(
                    detail={
                        "detail": "Non admin users can only create headsets within their own organization"
                    }
                )

        super().validate(attrs)
        return attrs


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "name", "course_id")

    def create(self, validated_data):
        user = self.context["request"].user

        if user.is_superuser:
            print("Hi! I'm a superuser")
            print(user)
            print(validated_data)
            if isinstance(validated_data["course_id"], int):
                course = Course.objects.get(id=validated_data["course_id"])
                student = Student.objects.create(
                    name=validated_data["name"], course_id=course
                )
                student.save()
                return student
            else:
                student = Student.objects.create(**validated_data)
                student.save()
                return student
        else:
            if isinstance(validated_data["course_id"], int):
                course = Course.objects.get(id=validated_data["course_id"])
                if course.staff_id.user is not self.request.user:
                    raise ValidationError
                else:
                    student = Student.objects.create(
                        name=validated_data["name"], course_id=course
                    )
                student.save()
                return student
            else:
                course = Course.objects.filter(staff_id=self.request.user)[0]
                student = Student.objects.create(
                    name=validated_data["name"], course_id=course
                )
                student.save()
                return student

    def validate(self, attrs):
        user = self.context["request"].user

        if not user.is_superuser:
            if user.id != attrs.staff_id:
                raise ValidationError(
                    detail={
                        "detail": "Non admin users can only add students to their own courses"
                    }
                )

        super().validate(attrs)
        return attrs


class GroupSerializer(serializers.ModelSerializer):
    members = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ("course_id", "headset_id", "members")
