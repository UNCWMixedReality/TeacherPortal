# users/views.py
from rest_framework import generics

from . import models, serializers


class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class StaffListView(generics.ListCreateAPIView):
    # TODO: Auth only + Logic to restrict list to only members of the same org
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer
