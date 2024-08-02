# models.py
from django.contrib.auth.models import User
from django.db import models
import uuid

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

