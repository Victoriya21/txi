from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/(\d+)/$', views.create, name='create'),

    url(r'^edit/(\d+)/$', views.edit, name='edit'),

    url(r'^check/(\d+)/$', views.check, name='check'),

    url(r'^download_file/(\d+)/$', views.download_file, name='download_file'),

    url(r'^(?P<lab_id>\d+)/$', views.detail, name='detail'),
]
