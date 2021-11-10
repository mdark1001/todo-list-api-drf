"""
@author: mdark1001
@date: 11/08/2021
"""
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('first_name','username','email')


class UserLoginSerializer(serializers.Serializer):
    """User login serializer """
    
    username = serializers.CharField(
        min_length=5,
        max_length=120
    )
    password = serializers.CharField(
        min_length=5,
        max_length=60,
    )

    def validate(self, attrs):
        """Valdite begin user's session """
        user = authenticate(username=attrs['username'],password=attrs['password'])
        if not user:
            raise serializers.ValidationError("Username or password are wrong, please check and try again")

        if not user.is_active:
            raise serializers.ValidationError(f"This username: {attrs['username']} is temporaly deactive")
        self.context['user']=user
        return attrs

    def create(self,data):
        """Return User and Token """
        token,created = Token.objects.get_or_create(user=self.context.get('user'))
        return self.context.get('user'),token.key