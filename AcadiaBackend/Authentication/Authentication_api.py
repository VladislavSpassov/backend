from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class UserSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password')


