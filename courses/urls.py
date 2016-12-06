from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CourseListView.as_view(), name='course_list'),

    url(r'^(?P<course_id>\d+)/$', views.detail, name='course_detail'),

    url(r'^create', views.create, name='course_create'),

    url(r'^edit/(?P<course_id>[0-9]+)/$', views.edit, name='course_edit'),

    url(r'^delete/(\d+)/$', views.delete, name='course_delete'),
    url(r'^(\d+)/delete/(\d+)/$', views.deleteTask, name='course_deleteTask'),
]
