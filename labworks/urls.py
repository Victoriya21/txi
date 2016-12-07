from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/(\d+)/$', views.create, name='lab_create'),

    url(r'^edit/(\d+)/$', views.edit, name='lab_edit'),

    url(r'^check/(\d+)/$', views.check, name='lab_check'),

    url(r'^download_file/(\d+)/$', views.download_file, name='download_file')
]
