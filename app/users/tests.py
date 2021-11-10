from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
# Create your tests here.

Users = get_user_model()

USER_LOGIN_URL = reverse('users-login')

class UsersApiTest(TestCase):
    """Users API Test """

    def setUp(self):
        self.user = Users.objects.create(
            username='Michael23',
            first_name = 'Michael J.',
            email='mich@thegoat.com'
        )
        self.user.set_password('Admin1234')
        self.user.save()
        self.client = APIClient()

    def test_login_successful(self):
        """Test over login user and return successful token and user info """
        response = self.client.post(USER_LOGIN_URL,{
            'username':'Michael23',
            'password':'Admin1234'
        })
        # print(type(res))
        #print(res.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIn('access_token',response.data.keys())

    def test_login_fail(self):
        response = self.client.post(USER_LOGIN_URL,{
            'username':'Michael23',
            'password':'Admin1234111'
        })
        #print(response.content)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
