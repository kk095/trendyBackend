from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import permissions



# Create your views here.

def home(request):
    return HttpResponse('hello')

class UserCreateView(CreateAPIView):
    model=get_user_model()
    serializer_class=UserSerializer
    permission_classes = [
        permissions.AllowAny 
    ]