from django.test import TestCase



from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create(email='test@example.com', first_name='test', last_name='user', gender='male', phone_number='1234567890')
        self.test_user.save()

    def test_signup(self):
        url = reverse('signup')
        data = {'email': 'user@example.com', 'first_name': 'user', 'last_name': 'test', 'gender': 'male', 'phone_number': '1234567890'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)

    def test_login(self):
        url = reverse('login')
        data = {'email': 'test@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('otp' in response.data)

    def test_logout(self):
        url = reverse('logout')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


