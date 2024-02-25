from django.test import Client, TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TaskTest(TestCase):
    def test_taskpage(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password ='test_user')
        self.client.login(username='test_user', password='test_user')
        response = self.client.get('tasks/')
        self.assertEqual(response.status_code, 200)

class ForgotTest(TestCase):
    def test_taskpage(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password ='test_user')
        self.client.login(username='test_user', password='test_user')
        response = self.client.get('forgot/')
        self.assertEqual(response.status_code, 200)