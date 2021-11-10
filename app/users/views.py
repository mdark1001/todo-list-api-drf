"""
@author: mdark1001
@date: 11/08/2021
"""

from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework import  viewsets,status,mixins
from rest_framework.decorators import action
from  rest_framework.response import Response
from users.serializers import UserModelSerializer,UserLoginSerializer
from django.contrib.auth import get_user_model

class UserView(viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    serializer_class=UserModelSerializer
    queryset = get_user_model().objects.filter(is_active=True)
    lookup_field ='username'

    @action(detail=False,methods=['POST'])
    def login(self,request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        data ={
            'user':UserModelSerializer(user).data,
            'access_token': token
        }

        return Response(data=data,status=status.HTTP_200_OK)