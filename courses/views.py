from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from courses.models import Course
from tasks.models import Task
from .forms import CourseForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test


class CourseListView(ListView):
    model = Course


def user_check(user):
    if user.groups.filter(name__in=['Students']) or user.groups.filter(name__in=['Teachers']) or user.is_superuser:
        return True
    else:
        return False


def student_check(user):
    if user.groups.filter(name__in=['Students']):
        return True
    else:
        return False


def admin_check(user):
    if user.groups.filter(name__in=['Teachers']) or user.is_superuser:
        return True
    else:
        return False


@user_passes_test(user_check)
def course_list(request, template_name='courses/course_list.html'):
    courses = Course.objects.all()
    data = {}
    data['object_list'] = courses
    return render(request, template_name, data)


@user_passes_test(user_check)
def detail(request, course_id):
    output = get_object_or_404(Course, id=course_id)
    context = {'one_course': output}
    return render(request, 'courses/one_course.html', context)


@user_passes_test(admin_check)
def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.professor = request.user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})


@user_passes_test(admin_check)
def edit(request, course_id):
    post = get_object_or_404(Course, pk=course_id)
    context = {'edit_course': post}
    if request.method == "POST":
        form = CourseForm(request.POST, instance=post)
        if form.is_valid():
            course = form.save()
            course.professor = request.user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=post)
    return render(request, 'courses/edit_course.html', context)


@user_passes_test(admin_check)
def delete(request, course_id):
    Course.objects.get(pk=course_id).delete()
    return HttpResponseRedirect("/courses")


@user_passes_test(admin_check)
def deleteTask(request, course_id, task_id):
    Task.objects.get(pk=task_id).delete()
    output = get_object_or_404(Course, id=course_id)
    context = {'one_course': output}
    return render(request, 'courses/one_course.html', context)
