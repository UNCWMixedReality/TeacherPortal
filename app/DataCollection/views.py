import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey

from .models import SessionData

# Create your views here.


class DataUploadView(APIView):
    permission_classes = [HasAPIKey | IsAuthenticated]

    # For first demo purposes, this is intentionally super accepeting of pretty much anything
    # as we make the system more resilient, we'll want to beef up the error checking here
    def post(self, request):
        new_session = SessionData.objects.create(data=request.data)

        new_session.save()

        return Response("Session Data Saved", status=200)
