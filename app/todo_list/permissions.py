"""
@author:mdark1001
@date: 11/08/2021
"""
from rest_framework.permissions import BasePermission
class IsOwnTask(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user