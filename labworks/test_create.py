# from multiprocessing.connection import Client
from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.test import Client
from courses.models import Course
from courses.forms import CourseForm
from labworks.models import Lab
from tasks.forms import TaskForm

from tasks.models import Task


class UserProfile(object):
    pass


class TestCreate(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testU1", password="111")
        gr = Group.objects.create(name='Teachers')
        gr.user_set.add(self.user)
        gr.save()
        self.user.save()
        self.newCourse = Course(name='testCourse', professor=self.user)
        self.newCourse.save()
        self.newTask = Task(course= self.newCourse, name='testTask', text='hahaha', points='20')
        self.newTask.save()
        self.newLabwork = Lab(name='testWork', mark='10', comment='amazing!', file='testFile.txt', task=self.newTask, author=self.user, condition='')
        self.newLabwork.save()

    def test_createform_task(self):
        form_data = {'name': 'formTest', 'text': 'testing form', 'points': '4'}
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_createform_course(self):
        form_data = {'name': 'testCourse'}
        form = CourseForm(data=form_data)
        self.assertTrue(form.is_valid())


class TestLoginPost(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_post(self):
        User.objects.create_user(username='admin', password='admin111')
        response = self.client.post('/', {'username': 'admin', 'password': 'admin111'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/courses/')

    def test_editCourse(self):
        u = User.objects.create_user(username='admin', password='admin111')
        self.client.post('/', {'username': 'admin', 'password': 'admin111'})
        Course.objects.create(name='NewCourse0', professor=u)
        response = self.client.post('/courses/edit/1/', {'name': 'NewCourse1', 'professor': u})
        self.assertEqual(response.status_code, 302)

    def test_coursecreate(self):
        u = User.objects.create_user(username='user', password='userpassword')
        response = self.client.post('/courses/create_course', {'name': 'Тестовый курс', 'professor': u})
        self.assertEqual(response.status_code, 302)

    def test_taskcreate(self):
        u = User.objects.create_user(username='user', password='userpassword')
        c = Course(name='testCourse', professor=u)
        response = self.client.post('/tasks/create',
                                    {'name': 'Тестовое задание', 'text': 'testing task', 'points': '4', 'course': c})
        self.assertEqual(response.status_code, 302)

    def test_labcreate(self):
        u = User.objects.create_user(username='user', password='userpassword')
        c = Course(name='testCourse', professor=u)
        t = Task(course=c, name='testTask', text='testtest', points='15')
        response = self.client.post('/labworks/create/1/',
                                    {'name': 'Тестовая лабораторная работа', 'author': u, 'mark': '5', 'comment': '',
                                     'task': t, 'file': ''})
        self.assertEqual(response.status_code, 302)


class TestPagesLoad(TestCase):
    def test_Pages(self):
        request = self.client.get('/courses/')
        self.assertEqual(request.status_code, 200)
        request2 = self.client.get('/courses/1/')
        self.assertEqual(request2.status_code, 302)
        request3 = self.client.get('/tasks/3/')
        self.assertEqual(request3.status_code, 302)
        request4 = self.client.get('/labworks/create/3/')
        self.assertEqual(request4.status_code, 302)
        request5 = self.client.get('/courses/edit/1/')
        self.assertEqual(request5.status_code, 302)
        request6 = self.client.get('/tasks/edit/37/')
        self.assertEqual(request6.status_code, 302)
        request7 = self.client.get('/labworks/edit/13/')
        self.assertEqual(request7.status_code, 302)
        request8 = self.client.get('/logout/')
        self.assertEqual(request8.status_code, 302)
        request9 = self.client.get('/courses/delete/1/')
        self.assertEqual(request9.status_code, 302)
        request10 = self.client.get('/labworks/check/1/')
        self.assertEqual(request10.status_code, 302)
        request11 = self.client.get('/courses/1/delete/1/')
        self.assertEqual(request11.status_code, 302)
