from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey
from users.models import Staff
from users.serializers import StaffSerializer

from .. import models, serializers


# /group/<str:id>/
class GroupByHeadsetIDView(APIView):
    serializer_class = serializers.GroupSerializer
    permission_classes = [HasAPIKey]

    def get(self, request, id):
        try:
            headset = models.Headset.objects.get(device_id=id)
            group = models.Group.objects.get(headset_id=headset)
            s_group = serializers.GroupSerializer(group)
            return Response(s_group.data)
        # These errors should return status codes as well, would clean the logic up clientside
        except models.Headset.DoesNotExist:
            return Response("Error - Headset is not registered")
        except models.Group.DoesNotExist:
            return Response("Error - Group not assigned")


# Headsets
# /headset/
class HeadsetCreateView(generics.CreateAPIView):
    serializer_class = serializers.HeadsetSerializer
    permission_classes = [HasAPIKey]


# /headset/exists/<str:id>/
class HeadsetExistsView(APIView):
    def get(self, request, id):

        try:
            headset = models.Headset.objects.get(  # noqa: F841
                device_id=id
            )  # retrieve the user using username
        except models.Headset.DoesNotExist:
            return Response(
                data={"registered": False}
            )  # return false as user does not exist
        else:
            return Response(data={"registered": True})  # Otherwise, return True


class HeadsetDetailView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request, id):
        try:
            headset = models.Headset.objects.get(device_id=id)
            h_data = serializers.HeadsetSerializer(headset).data
            return h_data
        except models.Headset.DoesNotExist:
            return Response("Error - Headset is not registered")
