from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import authenticate
# from account.models import User
from django.contrib.auth.models import User
from account.serializers import LoginSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your views here.
class UserView(APIView):
    def get(self, request):

        data=request.data

        user = User.objects.get(username=data['username'])

        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserCreationView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)

        if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(**serializer.validated_data)

        serialized = UserSerializer(user)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

class UserLogin(APIView):
    def post(self, request):
        try:
            serialized = LoginSerializer(data=request.data)

            serialized.is_valid()      

            username = request.data['username']
            password = request.data['password']
            
        except KeyError:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        # HTTP_400_BAD_REQUEST
        user = authenticate(username=username, password=password)

        if user:
            token = Token.objects.get_or_create(user=user)[0]

            return Response({'token': token.key})

        return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)