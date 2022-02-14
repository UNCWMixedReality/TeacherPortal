from django.urls import include, path

from . import views

urlpatterns = [
    path("organization/", views.OrganizationListCreateView.as_view()),
    path("organization/<int:pk>/", views.OrganizationDetailView.as_view()),
    path("organization/<int:pk>/staff/", views.OrganizationStaffListView.as_view()),
    path("organization/staff/", views.OrganizationStaffListView.as_view()),
    path("organization/<int:pk>/course/", views.OrganizationCourseListView.as_view()),
    path("organization/course/", views.OrganizationCourseListView.as_view()),
    path("organization/<int:pk>/headset/", views.OrganizationHeadsetListView.as_view()),
    path("organization/headset/", views.OrganizationHeadsetListView.as_view()),
    path("staff/", views.StaffCreateView.as_view()),
    path("staff/<int:pk>/", views.StaffDetailView.as_view()),
    path("staff/<int:pk>/course/", views.StaffCourseListView.as_view()),
    path("course/", views.CourseCreateView.as_view()),
    # path("course/<int:pk>/", views.CourseDetailView.as_view()),
    # path("course/<int:pk>/student/", views.CourseStudentListView.as_view()),
    # path("course/<int:pk>/group/", views.CourseGroupListView.as_view()),
    # path("student/", views.StudentCreateView.as_view()),
    # path("student/roster/", views.StudentRosterCreateView.as_view()),
    # path("student/<int:pk>/", views.StudentDetailView.as_view()),
    # path("group/", views.GroupCreateView.as_view()),
    # path("group/<int:pk>/", views.GroupDetailView.as_view()),
    # path("headset/", views.HeadsetCreateView.as_view()),
    # path("headset/<int:pk>/", views.HeadsetDetailView.as_view()),
]
