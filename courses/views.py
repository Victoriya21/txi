from django.views.generic import ListView

from courses.models import Course


class CourseListView(ListView):
    model = Course
