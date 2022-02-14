from re import S

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import Staff
from users.serializers import StaffSerializer

from . import models, serializers

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


# class CourseCreatListView(generics.ListCreateAPIView):
#     serializer_class = serializers.CourseSerializer
#     permissions_class = [IsAuthenticated]

#     def get_queryset(self):
#         pk = self.kwargs.get(URL_KWARG)
#         courses = models.Course.objects.filter(org_id=pk)
#         return courses
