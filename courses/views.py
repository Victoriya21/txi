from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from courses.models import Course
from tasks.models import Task
from .forms import CourseForm
from django.shortcuts import redirect


class CourseListView(ListView):
    model = Course


def detail(request, course_id):
    # output = Course.objects.get(id=course_id)
    output = get_object_or_404(Course, id=course_id)
    context = {'one_course': output}
    return render(request, 'courses/one_course.html', context)


def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.professor = request.user;
            course.save()
            return redirect('detail', course_id=course.pk)
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})


def delete(request, course_id):
    u = Course.objects.get(pk=course_id).delete()
    return HttpResponseRedirect("/courses")

def deleteTask(request, course_id, task_id):
    u = Task.objects.get(pk=task_id).delete()
    output = get_object_or_404(Course, id=course_id)
    context = {'one_course': output}
    return render(request, 'courses/one_course.html', context)