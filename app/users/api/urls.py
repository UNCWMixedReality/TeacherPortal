# users/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("staff/", views.StaffListView.as_view()),
]
