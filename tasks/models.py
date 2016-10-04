from django.db import models

from courses.models import Course
##from labworks.models import Lab


class Task(models.Model):
    course = models.ForeignKey(Course, related_name='courses')
    name = models.CharField(max_length=50)
    text = models.TextField()
    points = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{} on {}'.format(self.name, self.course)