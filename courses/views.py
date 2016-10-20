from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.template import loader
from django.views.generic import ListView

from courses.models import Course


class CourseListView(ListView):
    model = Course


def detail(request, course_id):
    output = Course.objects.filter(id=course_id)
    # template = loader.get_template('courses/one_course.html')
    # context = RequestContext(request, {
    #     'one_course': output,
    # })
    # return HttpResponse(template.render(context))
    # return HttpResponse(output)
    context = {'one_course': output}
    return render(request, 'courses/one_course.html', context)
