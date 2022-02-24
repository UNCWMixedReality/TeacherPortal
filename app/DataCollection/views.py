import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SessionData

# Create your views here.


class DataUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        new_session = SessionData.objects.create(data=request.data)

        new_session.save()

        return Response(None, status=200)
