from django.test import Client
from django.test import TestCase

from courses.forms import CourseForm
from tasks.forms import TaskForm
from labworks.forms import LabForm
from django.contrib.auth.models import User
from courses.models import Course

class TestCreate1(TestCase):
    def test_create(self):
        form_data = {'name': 'formTest', 'text': 'Form', 'points': '4'}
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())



class TestLogin2(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        res = response.__dir__()
        print(res)

    def test_editCourse(self):
        self.user = User.objects.create_user(username='admin', password='admin111')
        self.client.post('/', {'username': 'admin', 'password': 'admin111'})
        res = Course.objects.create(name='NewCourse', professor=self.user)
        self.client.post('/courses/edit/16/',{'name': 'NewCourse1', 'professor': self.user})
        res1 = self.client.get('/courses/1')
        print(self.user)
        print(res1.content)
        # self.assertEqual(res1.status_code, 200)
        # self.client.post('/courses/create_course', {'name' : 'SuperCourse'})
        # self.client.post('courses/edit/1/', {'name' : 'SuperCourseEdit'})
        # response = self.client.get('/courses/2/')
        # self.assertEqual(response.status_code, 302)






    # def test_upload(self):
    #     form_data = {'name': 'formTest', 'file': 'olololl.txt', 'mark': '0', 'comment': 'dfs'}
    #     form = LabForm(data=form_data)
    #     self.assertTrue(form.is_valid())


# class TestUpload(TestCase):
#     def setUp(self):
#         self.client = Client()
#         with open('Docy.doc') as fp:
            # self.client.post('/labworks/create/1/', {'name': 'User', 'file': fp))

# class TestLoginPost3(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_login_post(self):
#         User.objects.create_user(username='admin', password='admin111')
#         response = self.client.post('/', {'username': 'admin', 'password': 'admin111'})
#         self.assertRedirects(response, '/courses/')

        # self.assertTemplateUsed(response, 'registration/login.html', 'base.html')

        # response2 = self.client.post('/', {'username': 'student1', 'password': 'qwertyui1'})
        # self.assertEquals(response2.status_code, 200)
        # response3 = self.client.post('/', {'username': 'teacher1', 'password': 'qwertyui2'})
        # self.assertEquals(response3.status_code, 200)