from django.conf.urls import url

from courses.views import CourseListView

urlpatterns = [
    url(r'^$', CourseListView.as_view(), name='course_list'),
]