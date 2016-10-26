from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from courses.models import Course


class CourseListView(ListView):
    model = Course


def detail(request, course_id):
    # output = Course.objects.get(id=course_id)
    output = get_object_or_404(Course, id=course_id)
    context = {'one_course': output}
    return render(request, 'courses/one_course.html', context)
