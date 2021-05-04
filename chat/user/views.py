from django.shortcuts import render
from user.serializers import UserSerializer
from user.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from django.db.models import Q, F, Value
from rest_framework import status
import csv
#from rest_framework_jwt.settings import api_settings
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#from rest_framework.permissions import IsAuthenticated


class UserDetail(APIView):
    def get(self, request, format=None):
        res = {}
        user = User.objects.get(email = request.query_params["email"])
        if user.check_password(request.query_params["password"]):
            print(user)
            serializer = UserSerializer(user, many=False)
            #jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            #jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            #payload = jwt_payload_handler(user)
            #token = jwt_encode_handler(payload)
            data =serializer.data
            res = {'data':data}
            #data['token'] = 
        else:
            res = {'error':'credecenciales erroneas'}
        return Response({'data':data})
    

    def post(self, request, format=None):
        user_data = {
            "username" :request.data["email"].split('@')[0],
            "email" : request.data["email"],
            "password" : request.data["password"],
        }
        print (user_data)
        user = User.objects.create_user(username = user_data["username"], email =user_data["email"], password = user_data["password"])
        print('holal',user.username)
        serializer = UserSerializer(data = user)
        if serializer.is_valid():
            serializer.save()
        return Response({'status' : 'ok','descripcion': 'usuario creado'},status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



