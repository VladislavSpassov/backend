from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import viewsets
from .Authentication_api import UserSerialiser
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework import generics


from .models import User

# Create your views here.


class ListUsersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = User.objects.all()
    serializer_class = UserSerialiser
