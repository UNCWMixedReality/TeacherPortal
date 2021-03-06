# api/urls.py
from django.urls import include, path

urlpatterns = [
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("", include("organizations.api.urls")),
    path("", include("DataCollection.urls")),
]
