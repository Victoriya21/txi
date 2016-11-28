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


class TestLoginPost(TestCase):
    def test_login_post(self):
        User.objects.create_user(username='admin', password='admin111')
        response = self.client.post('/', {'username': 'admin', 'password': 'admin111'})
        self.assertRedirects(response, '/courses/')

    def test_editCourse(self):
        u = User.objects.create_user(username='admin', password='admin111')
        gr = Group.objects.create(name='Teachers')
        gr.user_set.add(u)
        gr.save()
        self.client.force_login(u)
        Course.objects.create(name='NewCourse0', professor=u)
        self.client.post('/courses/edit/1/', {'name': 'NewCourse1', 'professor': u})
        self.assertEqual(Course.objects.get().name, 'NewCourse1')

    def test_coursecreate(self):
        u = User.objects.create_user(username='user', password='userpassword')
        gr = Group.objects.create(name='Teachers')
        gr.user_set.add(u)
        gr.save()
        self.client.force_login(u)
        self.client.post('/courses/create_course', {'name': 'Test Course', 'professor': u})
        self.assertEqual(Course.objects.get().name, 'Test Course')

    def test_taskcreate(self):
        u = User.objects.create_user(username='user', password='userpassword')
        gr = Group.objects.create(name='Teachers')
        gr.user_set.add(u)
        gr.save()
        self.client.force_login(u)
        c = Course.objects.create(name='testCourse', professor=u)
        Task.objects.create(name='Test Task', text='testing task', points='4', course=c)
        self.assertEqual(Task.objects.get().name, 'Test Task')

    def test_labcreate(self):
        u2 = User.objects.create_user(username='user2', password='userpassword2')
        gr2 = Group.objects.create(name='Teachers')
        gr2.user_set.add(u2)
        gr2.save()
        self.client.force_login(u2)
        c = Course.objects.create(name='testCourse', professor=u2)
        t = Task.objects.create(course=c, name='testTask', text='testtest', points='15')
        self.client.logout()
        u = User.objects.create_user(username='user', password='userpassword')
        gr = Group.objects.create(name='Students')
        gr.user_set.add(u)
        gr.save()
        self.client.force_login(u)
        with open(__file__) as fp:
            self.client.post(
                '/labworks/create/1/',
                {'name': 'Тестовая лабораторная работа', 'author': u, 'mark': '5', 'comment': 'dfsd',
                 'task': t, 'file': fp})
        lab = Lab.objects.get()
        self.assertEqual(lab.author, u)
        self.assertEqual(lab.mark, 5)
        self.assertEqual(lab.comment, 'dfsd')
