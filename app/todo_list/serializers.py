"""
@author: mdark1001
@date: 11/06/2021
"""
from rest_framework import serializers
from django.conf import settings
from todo_list.models import Task

class TaskSerializer(serializers.Serializer):
    """Serializer for Task model """
    name = serializers.CharField(
        max_length=120,
        min_length=2,
    )
    slug = serializers.CharField(
        required=False,
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
        # validated_data['user'] = self.request.user
        return Task.objects.create(**validated_data)
    

