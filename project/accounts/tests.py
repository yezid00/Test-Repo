
from django.urls import reverse
from rest_framework import status

from project.accounts.models import User
from project.common.tests import BaseTestCase


class RegistrationTestCase(BaseTestCase):
    EMAIL = 'user@mail.com'
    PASSWORD = 'RealSecure123'

    def setUp(self):
        super().setUp()
        self.registration_url = reverse('rest_register')

    def test_cannot_register_when_passwords_dont_match(self):
        self.assertFalse(User.objects.exists())
        response = self.client.post(
            self.registration_url,
            data={
                'email': self.EMAIL,
                'password1': self.PASSWORD,
                'password2': self.PASSWORD + 'llama',
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'], ["The two password fields didn't match."])
        self.assertFalse(User.objects.exists())

    def test_cannot_register_when_password_too_short(self):
        self.assertFalse(User.objects.exists())
        response = self.client.post(
            self.registration_url,
            data={
                'email': self.EMAIL,
                'password1': 'pwd',
                'password2': 'pwd',
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password1'], ["This password is too short. It must contain at least 8 characters."])
        self.assertFalse(User.objects.exists())

    def test_cannot_register_when_password_too_common(self):
        self.assertFalse(User.objects.exists())
        response = self.client.post(
            self.registration_url,
            data={
                'email': self.EMAIL,
                'password1': 'password',
                'password2': 'password',
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password1'], ["This password is too common."])
        self.assertFalse(User.objects.exists())

    def test_cannot_register_when_password_entirely_numeric(self):
        self.assertFalse(User.objects.exists())
        response = self.client.post(
            self.registration_url,
            data={
                'email': self.EMAIL,
                'password1': '93586033',
                'password2': '93586033',
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password1'], ["This password is entirely numeric."])
        self.assertFalse(User.objects.exists())

    def test_can_register_with_matching_secure_passwords(self):
        self.assertFalse(User.objects.exists())
        response = self.client.post(
            self.registration_url,
            data={
                'email': self.EMAIL,
                'password1': self.PASSWORD,
                'password2': self.PASSWORD,
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['detail'], 'Verification e-mail sent.')
        self.assertTrue(User.objects.filter(email=self.EMAIL).exists())

