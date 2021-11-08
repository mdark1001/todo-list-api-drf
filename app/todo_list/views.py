"""
@author: mdark1001
@date: 11/06/2021
"""
from rest_framework.generics import GenericAPIView, ListAPIView,CreateAPIView
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todo_list.permissions import IsOwnTask
from todo_list.serializers import TaskSerializer
from todo_list.models import Task


class TaskListView(ListAPIView,CreateAPIView):
    """List user taks """
    # queryset =
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskUpdateRetrieveView(GenericAPIView, 
            mixins.UpdateModelMixin,
            mixins.RetrieveModelMixin):

    """Update and retrieve tasks  """

    serializer_class =TaskSerializer
    permission_classes = [IsAuthenticated,IsOwnTask]
    lookup_field = 'slug'
    queryset = Task.objects.all()

    def put(self,request,*args,**kwargs):
        """Update task information. """
        return self.partial_update(request, *args, **kwargs)
    def get(self,request, *args,**kwargs):
        """Get a specific task using slugname """
        return self.retrieve(request, *args,**kwargs)
