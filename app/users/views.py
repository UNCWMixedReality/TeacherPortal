from DataCollection.models import ScheduledSession
from django.db.models import Case, When
from django.shortcuts import render

# Create your views here.


def HomepageView(request):
    upcoming = ScheduledSession.objects.order_by("date")[:5]
    return render(request, "users/home.html", {"sessions": upcoming})
