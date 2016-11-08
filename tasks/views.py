from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Task
from courses.models import Course
from .forms import TaskForm
from django.shortcuts import redirect

@login_required
def detail(request, task_id):
    output = get_object_or_404(Task, id=task_id)
    context = {'one_task': output}
    return render(request, 'tasks/one_task.html', context)


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.course = Course.objects.get(id=2)
            task.save()
            return redirect('detail', task_id=task.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})
