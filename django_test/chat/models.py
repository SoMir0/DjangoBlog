from datetime import datetime
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=40, unique=True, blank=False)

class Message(models.Model):
    author = models.CharField(max_length=40)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=40)
