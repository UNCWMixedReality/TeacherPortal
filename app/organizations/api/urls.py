from django.urls import include, path

from . import views

urlpatterns = [
    path("group/<str:id>/", views.GroupByHeadsetIDView.as_view()),
    path("headset/", views.HeadsetCreateView.as_view()),
    path("headset/exists/<str:id>/", views.HeadsetExistsView.as_view()),
    path("headset/<str:id>/", views.HeadsetDetailView.as_view()),
]
