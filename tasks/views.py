from django.shortcuts import render, get_object_or_404
from .models import Task
from courses.models import Course
from .forms import TaskForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test


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
def detail(request, task_id):
    output = get_object_or_404(Task, id=task_id)
    context = {'one_task': output}
    return render(request, 'tasks/one_task.html', context)


@user_passes_test(admin_check)
def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.course = Course.objects.get(id=course_id)
            task.save()
            return redirect('http://127.0.0.1:8000/courses/'+courseId, task_id=task.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


@user_passes_test(admin_check)
def edit(request, task_id):
    global idnew
    post = get_object_or_404(Task, pk=task_id)
    context = {'edit_task': post}

    if request.method == "POST":
        courseId = request.POST.get('course_id')
        convertId = int('0' + courseId)

        all_courses = Course.objects.all()
        for id_course in all_courses:
            if id_course.pk == convertId:
                idnew = id_course

        form = TaskForm(request.POST, instance=post)
        if form.is_valid():
            task = form.save()
            task.course = idnew
            task.save()
            return redirect('http://127.0.0.1:8000/courses/'+courseId, task_id=task.pk)
    else:
        form = TaskForm(instance=post)
    return render(request, 'tasks/edit_task.html', context)


@user_passes_test(admin_check)
def delete(request, course_id, task_id):
    Task.objects.get(pk=task_id).delete()
    output = get_object_or_404(Course, id=course_id)
    context = {'one_course': output}
    return render(request, 'courses/one_course.html', context)
