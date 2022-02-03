from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.OrganizationListCreateView.as_view()),
    path("course/", views.CourseListCreateView.as_view()),
]
