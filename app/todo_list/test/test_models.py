"""
@date: 11/06/2021
@author: mdark1001
"""

from django.test import TestCase
from rest_framework.test import APIClient
from slugify.slugify import slugify
from todo_list.models import Task
from django.contrib.auth import get_user_model
from datetime import date
from slugify import  slugify

Users = get_user_model()
class TaksTest(TestCase):
    def setUp(self):
        self.user = Users.objects.create(
            username='superUser123',    
            #name='Adminstrator',
        )


    def test_create_task(self):
        """Create multiple tasks for an user """
        tasks =[
            {
                'name':'Take out the garbase',
                'planned':date.today(),
                'priority':3,
                'user': self.user,
            },
             {
                'name':'Make coffee',
                'planned':date.today(),
                'priority':5,
                'user': self.user,
            }
        ]
        for task in tasks:
            Task.objects.create(**task)
        self.assertEqual(len(tasks),Task.objects.filter(user=self.user).count())

    def test_slugname(self):
        """Test if save method works without slugname"""
        task_data = {
                'name':'Take out the garbase',
                'planned':date.today(),
                'priority':3,
                'user': self.user,
            }
        task = Task.objects.create(**task_data)
        self.assertEqual(slugify(task_data['name']),task.slug)
    
    def test_task_uncompleted(self):
        """Create multiple tasks for an user """
        tasks =[
            {
                'name':'Take out the garbase',
                'planned':date.today(),
                'priority':3,
                'user': self.user,
                'completed':True
            },
             {
                'name':'Make coffee',
                'planned':date.today(),
                'priority':5,
                'user': self.user,
                'completed':False,
            }
        ]
        for task in tasks:
            Task.objects.create(**task)
        completed = Task.task_compled.count()
        # print(completed)
        completed_data  = len(list(filter(lambda s: s['completed'],tasks)))
        
        self.assertEqual(completed_data, completed)
