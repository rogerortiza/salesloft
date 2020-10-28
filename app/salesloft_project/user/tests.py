from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

TOKEN_URL = reverse('user:token')


class PublicUsersApiTests(TestCase):
    """ Test the users API """

    def setUp(self):
        self.client = APIClient()

    def _create_user(self, **params):
        return get_user_model().objects.create_user(**params)

    def test_create_token_for_user(self):
        """ Test that the token is created for a valid user """
        payload = {'username': 'developer', 'password': 'Test123test'}
        self._create_user(**payload)
        response = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_token_with_invalid_credentials(self):
        """
        Test that the token is won't be created if invalid credentials are
        given
        """
        new_user = {'username': 'developer', 'password': 'Test123test'}
        self._create_user(**new_user)
        payload = {'username': 'developer', 'password': 'wrong_pass'}
        response = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """" Test that the token is not created if user doesn't exist """
        payload = {'username': 'developer', 'password': 'wrong_pass'}
        response = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """ Test that the username and password are required """
        response = self.client.post(TOKEN_URL, {'username': 'user', 'password': ''})
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
