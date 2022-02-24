from django.urls import path

from . import views

urlpatterns = [path("new-session-data/", views.DataUploadView.as_view())]
