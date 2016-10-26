from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    professor = models.ForeignKey(User)
    # professor = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return '{0} by {1}'.format(self.name, self.professor)
