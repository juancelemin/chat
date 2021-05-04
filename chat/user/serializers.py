from rest_framework import serializers
from user.models import User
import datetime as dt
import json
from rest_framework import exceptions

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password','last_login','is_staff','is_active','date_joined','user_permissions','groups')
        
    def to_representation(self, value):
        ret = {
            "idUsuario": value.id,
            "superUsurio": value.is_superuser,
            "userName": value.username,
            "nombreUsuario": value.first_name,
            "apellidoUsuario": value.last_name,
        }
        return ret
    
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

