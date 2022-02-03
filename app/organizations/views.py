from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, serializers


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseListCreateView(generics.ListCreateAPIView):
    # TODO: Auth only + Logic to restrict list to only members of the same org
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
