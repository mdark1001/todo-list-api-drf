"""
@author: mdark1001
@date: 11/06/2021
"""
from rest_framework import serializers
from todo_list.models import Task

class TaskSerializer(serializers.Serializer):
    """Serializer for Task model """
    name = serializers.CharField(
        max_length=120,
        min_length=2,
    )
    slug = serializers.CharField(
        required=False,
        read_only=True,
    )
    planned = serializers.DateField(

    )
  
    completed =serializers.BooleanField(
        default=False,
    )
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    def create(self,validated_data):
        """Create a new task for user logged in request  """
        return Task.objects.create(**validated_data)
    def update(self,obj,validated_data):
        """Update partial task information.  """
        Task.objects.filter(pk=obj.pk).update(**validated_data)
        task = Task.objects.get(pk=obj.pk)
        return task
