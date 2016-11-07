from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<task_id>\d+)/$', views.detail, name='detail'),
    url(r'^create', views.create, name='create')
]
