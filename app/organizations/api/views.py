from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from users.models import Staff
from users.serializers import StaffSerializer

from .. import models, serializers

URL_KWARG = "pk"

# ==============================================================================
# ORGANIZATION

# /organization/
class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [IsAuthenticated]


# /organization/<int:pk>/
class OrganizationDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get(URL_KWARG)
        org = models.Organization.objects.filter(id=pk)
        return org


# /organization/<int:pk>/staff and /organization/staff
class OrganizationStaffListView(generics.ListAPIView):
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if (self.request.user.is_superuser) and (URL_KWARG in self.kwargs):
            return Staff.objects.filter(organization=self.kwargs.get(URL_KWARG))
        else:
            staff = Staff.objects.get(user=self.request.user)
            return Staff.objects.filter(organization=staff.organization)


# /organization/<int:pk>/course and /organization/course
class OrganizationCourseListView(generics.ListAPIView):
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if (self.request.user.is_superuser) and (URL_KWARG in self.kwargs):
            return models.Course.objects.filter(org_id=self.kwargs.get(URL_KWARG))
        else:
            staff = Staff.objects.get(user=self.request.user)
            return models.Course.objects.filter(org_id=staff.organization)


# /organization/<int:pk>/headset/ and /organization/headset
class OrganizationHeadsetListView(generics.ListAPIView):
    serializer_class = serializers.HeadsetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if (self.request.user.is_superuser) and (URL_KWARG in self.kwargs):
            return models.Headset.objects.filter(org_id=self.kwargs.get(URL_KWARG))
        else:
            staff = Staff.objects.get(user=self.request.user)
            return models.Headset.objects.filter(org_id=staff.organization)


# ==============================================================================
# Staff

# /staff/
class StaffCreateView(generics.CreateAPIView):
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]


# /staff/<int:pk>/
class StaffDetailView(generics.RetrieveAPIView):
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "user_id"
    lookup_url_kwarg = "pk"
    queryset = Staff.objects.all()


# /staff/<int:pk>/course/
class StaffCourseListView(generics.ListAPIView):
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Course.objects.filter(staff_id=self.kwargs.get(URL_KWARG))


# Courses
# /course/
class CourseCreateView(generics.CreateAPIView):
    serializer_class = serializers.CourseSerializer
    permissions_classes = [IsAuthenticated]


# /course/<int:pk>/
class CourseDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Course.objects.all()
        else:
            course = models.Course.objects.get(id=self.kwargs.get(URL_KWARG))
            staff = Staff.objects.get(user=self.request.user)
            if staff.organization == course.org_id:
                return models.Course.objects.all()
            else:
                raise ValidationError(
                    detail="Only Courses from your parent organization can be viewed"
                )


# /course/<int:pk>/student/ and /course/student/
class CourseStudentListView(generics.ListAPIView):
    serializer_class = serializers.StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if (self.request.user.is_superuser) and (URL_KWARG in self.kwargs):
            return models.Student.objects.filter(course_id=self.kwargs.get(URL_KWARG))
        else:
            course = models.Course.objects.get(staff_id=self.request.user)
            return models.Student.objects.filter(course_id=course)


# /course/<int:pk>/groups/ and /course/groups
class CourseGroupListView(generics.ListAPIView):
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if (self.request.user.is_superuser) and (URL_KWARG in self.kwargs):
            return models.Group.objects.filter(course_id=self.kwargs.get(URL_KWARG))
        else:
            course = models.Course.objects.filter(staff_id__pk=self.request.user.id)[0]
            return models.Group.objects.filter(course_id=course)


# Students
# /student/
class StudentCreateView(generics.CreateAPIView):
    serializer_class = serializers.StudentSerializer
    permission_classes = [IsAuthenticated]


# # /student/roster
# class StudentRosterView(APIView):

#     def _create_student(self, student_name, course):
#         student = models.Student.object.create(
#             name=student_name,
#             course_id=course
#         )


# /student/<int:pk>/
class StudentDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.StudentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Student.objects.all()
        else:
            staff = Staff.objects.get(user=self.request.user)
            courses = [
                course.id
                for course in models.Course.objects.filter(
                    organization=staff.organization
                )
            ]
            course = models.Student.objects.filter(course_id__in=courses)
            return course


# Groups
# /group/
class GroupDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Group.objects.all()
        else:
            staff = Staff.objects.get(user=self.request.user)
            courses = [
                course.id
                for course in models.Course.objects.filter(
                    organization=staff.organization
                )
            ]
            course = models.Group.objects.filter(course_id__in=courses)
            return course


# Headsets
# /headset/
class HeadsetCreateView(generics.CreateAPIView):
    serializer_class = serializers.HeadsetSerializer
    permission_classes = [IsAuthenticated]


# /headset/<int:pk>/
class HeadsetDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.HeadsetSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Headset.objects.all()
        else:
            staff = Staff.objects.get(user=self.request.user)
            headsets = models.Headset.objects.filter(org_id=staff.organization)
            return headsets
