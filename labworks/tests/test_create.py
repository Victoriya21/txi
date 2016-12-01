from django.contrib.auth.models import User, Group
from django.test import TestCase
from courses.forms import CourseForm
from courses.models import Course
from labworks.models import Lab
from tasks.forms import TaskForm
from tasks.models import Task


class TestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testU1", password="111")
        gr = Group.objects.create(name='Teachers')
        gr.user_set.add(self.user)
        gr.save()
        self.user.save()
        self.newCourse = Course(name='testCourse', professor=self.user)
        self.newCourse.save()
        self.newTask = Task(course=self.newCourse, name='testTask', text='hahaha', points='20')
        self.newTask.save()
        self.newLabwork = Lab(name='testWork', mark='10', comment='amazing!', file='testFile.txt', task=self.newTask, author=self.user, condition='')
        self.newLabwork.save()

    def test_createform_task(self):
        form_data = {'name': 'formTest', 'text': 'testing form', 'points': '4'}
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_createform_task_invalid(self):
        form_data = {'name': 'formTest', 'text': 'testing form', 'points': '4!'}
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_createform_course(self):
        form_data = {'name': 'testCourse'}
        form = CourseForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_createform_course_invalid(self):
        form_data = {'name': ''}
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())