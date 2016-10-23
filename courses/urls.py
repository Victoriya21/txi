from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CourseListView.as_view(), name='course_list'),
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
]
