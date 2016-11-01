from django.conf.urls import url
from django.conf import settings ##added
from django.conf.urls.static import static ##added

from . import views

urlpatterns = [
  ##  url(r'^create', views.create, name='create'),
    url(r'^create/(\d+)/$', views.create, name='create'),
    url(r'^(?P<lab_id>\d+)/$', views.detail, name='detail'),
 ##   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT), ##added
]
