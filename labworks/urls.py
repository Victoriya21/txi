from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create', views.create, name='create'),
    url(r'^(?P<lab_id>\d+)/$', views.detail, name='detail'),
]
