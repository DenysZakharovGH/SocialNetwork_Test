
from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User



class CreateUserTest(APITestCase):
    def setUp(self):
        self.data = {
                    "username": 'mike',
                    "password1": 'johnpassword',
                    "password2": 'johnpassword'
                    }

    def test_can_create_user(self):
        response = self.client.post(reverse('rest_register'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReadUserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="mike")
        print(self.user)

    def test_can_any_read_user_list(self):# user list can read only superuser
        response = self.client.get(reverse('get_post_users'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CreatePostTest(APITestCase):
    def setUp(self):
        self.data = {
            "body": "body test",
            "title": "Post test",
            "author": 1
        }

    def test_can_add_post_not_auth(self):
        response = self.client.post(reverse('user-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class LoginUserTest(APITestCase):

    def setUp(self):
        self.data = {
            "username": 'mike',
            "email": "",
            "password": 'johnpassword'
        }
    def test_can_add_post_not_auth(self):
        response = self.client.post(reverse('rest_login'), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            "username": 'mike',
            "password": 'johnpassword'
        }
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('http://127.0.0.1:8000/auth/login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # should be logged in now
       # self.assertTrue(response.context['user'].is_active)

