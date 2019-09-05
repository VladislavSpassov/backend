

from django.db import models
from django.conf import settings


class User(models.Model):

    username = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username
