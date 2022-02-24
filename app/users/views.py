from django.db.models import Case, When
from django.shortcuts import render

# Create your views here.


def HomepageView(request):
    return render(request, "users/home.html", {})
