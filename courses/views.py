from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from courses.models import Course
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
