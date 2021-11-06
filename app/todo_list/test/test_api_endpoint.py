"""
@author: mdark1001
@date: 11/06/2021
"""
from datetime import date,timedelta

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from django.contrib.auth import get_user_model


from slugify import  slugify
from todo_list.models import Task

Users = get_user_model()

TASK_URL = reverse('tasks:list')

USERNAME = 'SuperAdmin123'
USER_PASSWORD = 'password123456'

class TaksApiEndpointsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
      
        self.user=Users.objects.create(username=USERNAME)
        self.user.set_password(USER_PASSWORD)
        self.user_two = Users.objects.create(username='Another User')

        self.tasks = [
                     {
                'name':'Take out the garbage',
                'planned':date.today(),
                'priority':3,
                'user': self.user_two,
            },
             {
                'name':'Make coffee',
                'planned':date.today(),
                'priority':5,
                'user': self.user_two,
            },
              {
                'name':'Make the bed',
                'planned':date.today() + timedelta(days=2) ,
                'priority':1,
                'user': self.user_two,
            },
             {
                'name':'Do the homework',
                'planned':date.today() + timedelta(days=1) ,
                'priority':3,
                'user': self.user,
            },

        ]
        for task in self.tasks:
            Task.objects.create(**task)

    
    def test_list_task_fail(self):
        """Fail list tasks we must be authenticated  """
        res = self.client.get(TASK_URL)
        self.assertEqual(res.status_code,status.HTTP_403_FORBIDDEN)

    def test_list_taks(self):
        self.client.login(
            username = USERNAME,
            password=USER_PASSWORD,
        )
        self.client.force_authenticate(
          user=self.user
        )
        total_taks_user = len(list(filter(lambda t: t['user']==self.user,self.tasks)))
        #print(self.user)
        res = self.client.get(TASK_URL)
        print(res.content)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.data['count'],total_taks_user)

    def test_create_taks(self):
        """Create a task using endpoint"""
        self.client.force_authenticate(
          user=self.user
        )
        res =self.client.post(TASK_URL,{
                'name':'Take out the garbage',
                'planned':date.today(),
                'priority':3,
                #'user': self.user,
            })
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        res = self.client.get(TASK_URL)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertIn('results',res.data)

    