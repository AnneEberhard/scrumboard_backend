from django.test import Client, TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.core import mail


# Create your tests here.
class WithinJoinTest(TestCase):
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
        return token

    def test_taskpage(self):
        token = self.authenticate_user('test_user', 'test_user')
        response = self.client.get('/tasks/', HTTP_AUTHORIZATION=f'Token {token}')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_subtaskpage(self):
        token = self.authenticate_user('test_user', 'test_user')
        response = self.client.get('/subTasks/', HTTP_AUTHORIZATION=f'Token {token}')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_categoriespage(self):
        token = self.authenticate_user('test_user', 'test_user')
        response = self.client.get('/savedCategories/', HTTP_AUTHORIZATION=f'Token {token}')
        print(response)
        self.assertEqual(response.status_code, 200)
        
    def test_contactspage(self):
        token = self.authenticate_user('test_user', 'test_user')
        response = self.client.get('/contacts/', HTTP_AUTHORIZATION=f'Token {token}')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_logoutpage(self):
        token = self.authenticate_user('test_user', 'test_user')
        response = self.client.post('/logout/', HTTP_AUTHORIZATION=f'Token {token}')
        print(response)
        self.assertEqual(response.status_code, 200)


class RegistrationViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_registration(self):
        registration_data = {
            'username': 'test_user',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'test_password',
        }

        response = self.client.post('/register/', registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='test_user').exists())
        user = User.objects.get(username='test_user')
        self.assertTrue(user.check_password('test_password'))


class ForgotViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_user', email='test@example.com')

    def test_forgot_successful(self):
        forgot_data = {
            'email': 'test@example.com',
        }

        response = self.client.post('/forgot/', forgot_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('exists', response.data)
        self.assertTrue(response.data['exists'])
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['test@example.com'])

    def test_forgot_nonexistent_user(self):
        forgot_data = {
            'email': 'nonexistent@example.com',
        }

        response = self.client.post('/forgot/', forgot_data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('exists', response.data)
        self.assertFalse(response.data['exists'])
        self.assertEqual(len(mail.outbox), 0)


