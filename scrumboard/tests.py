from django.test import Client, TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TaskTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_user')
        
    def test_login(self):
        response = self.client.post('/login/', {'username': 'test_user', 'password': 'test_user'})
        self.assertEqual(response.status_code, 200)

    def authenticate_user(self, username, password):
        response = self.client.post('/login/', {'username': username, 'password': password})
        self.assertEqual(response.status_code, 200)
        token = response.data.get('token') 
        print(f"Hallo, {token}")
        return token


    def test_taskpage(self):
        token = self.authenticate_user('test_user', 'test_user')
        print(f"Hallo again, {token}")
        response = self.client.get('/tasks/', HTTP_AUTHORIZATION=f'Token {token}')
        print(response)
        self.assertEqual(response.status_code, 200)


        