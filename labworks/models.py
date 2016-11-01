from django.contrib.auth.models import User
from django.db import models
from courses.models import Course
from labsmonitor import settings
from tasks.models import Task


class Lab(models.Model):
    name = models.CharField(max_length=50)
    mark = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField()

    CONDITION_CHECKED = 'checked'
    CONDITION_NOT_CHECKED = 'not checked'
    CONDITION_CHOICES = (
        (CONDITION_CHECKED, 'Проверена'),
        (CONDITION_NOT_CHECKED, 'Не проверена'),
    )
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, default=CONDITION_NOT_CHECKED)  # исправить?

    ##file = models.CharField(max_length=250)
    file = models.FileField()
    task = models.ForeignKey(Task, related_name='tasks')
    author = models.ForeignKey(User)

    def __str__(self):
        return '{} on {}'.format(self.name, self.task)

  #  def handle_uploaded_file(f):  ##added
  #      with open('/srv/media/somefile.txt', 'wb+') as destination:
  #         for chunk in f.chunks():
  #               destination.write(chunk)
