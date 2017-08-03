from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Room(models.Model):
    text = models.CharField(max_length=200)
    def __str__(self):
        return 'Room:' + self.text
class LiveRoom(models.Model):
    room_id=models.IntegerField(primary_key=True)
    room_name=models.CharField(max_length=100)
    room_introduction=models.TextField()
    room_img=models.ImageField(upload_to='liveroomimg')
    room_creater=models.CharField(max_length=100)
    created_time=models.DateTimeField()
class VideoRoom(models.Model):
    room_id=models.IntegerField(primary_key=True)
    room_name=models.CharField(max_length=100)
    room_introduction=models.TextField()
    room_img=models.ImageField(upload_to='videoroomimg')
    room_creater=models.CharField(max_length=100)
    created_time=models.DateTimeField()
    videofile=models.FileField()
    time_length=models.IntegerField()
class AllSilent(models.Model):
    room_id=models.IntegerField()
    is_allsilent=models.BooleanField()
    silent_time=models.DateTimeField()
class OneSilent(models.Model):
    room_id=models.IntegerField()
    user=models.CharField(max_length=100)
    is_silent=models.BooleanField()
    silent_time=models.DateTimeField()
class ChatHistory(models.Model):
    room_id=models.IntegerField()
    user=models.CharField(max_length=100)
    content=models.TextField()
    time=models.DateTimeField()
class VisitHistory(models.Model):
    room_id=models.IntegerField()
    user=models.CharField(max_length=100)
    visit_time=models.DateTimeField()
    leave_time=models.DateTimeField()
    is_refused=models.BooleanField()
