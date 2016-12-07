from django.contrib.auth.models import User
from django.db import models

from tasks.models import Task


class Lab(models.Model):
    name = models.CharField(max_length=50)
    mark = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField()

    CONDITION_CHECKED = 'Проверена'
    CONDITION_NOT_CHECKED = 'Не проверена'
    CONDITION_CHOICES = (
        (CONDITION_CHECKED, 'Проверена'),
        (CONDITION_NOT_CHECKED, 'Не проверена'),
    )
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, default=CONDITION_NOT_CHECKED)

    file = models.FileField()
    task = models.ForeignKey(Task, related_name='labs')
    author = models.ForeignKey(User)

    def __str__(self):
        return '{} on {}'.format(self.name, self.task)
