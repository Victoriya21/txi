from django.contrib.auth.models import User, Group
from django.test import TestCase
from courses.models import Course
from labworks.models import Lab
from tasks.models import Task


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
                {'name': 'Тестовая лабораторная работа', 'author': u, 'mark': '5', 'comment': 'Отлично',
                 'task': t, 'file': fp})
        lab = Lab.objects.get()
        self.assertEqual(lab.author, u)
        self.assertEqual(lab.mark, 5)
        self.assertEqual(lab.comment, 'Отлично')
        
