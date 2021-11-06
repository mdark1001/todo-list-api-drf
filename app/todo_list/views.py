"""
@author: mdark1001
@date: 11/06/2021
"""
from rest_framework.generics import  ListAPIView,CreateAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from todo_list.serializers import TaskSerializer
from todo_list.models import Task


class TaskListView(ListAPIView,CreateAPIView):
    """List user taks """
    # queryset =
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    