from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<task_id>\d+)/$', views.detail, name='taskDetail'),

    url(r'^create/(\d+)/$', views.create, name='task_create'),

    url(r'^edit/(?P<task_id>[0-9]+)/$', views.edit, name='edit'),

    url(r'^(\d+)/delete/(\d+)/$', views.delete, name='deleteTask')
]
