from .models import Room, MyUser, LiveRoom
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('text',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('account', 'nickname', 'is_student',
                  'is_active', 'is_admin', 'password')

class LiveRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveRoom
        fields = ('room_id', 'room_name', 'room_introduction',
                  'room_img', 'room_creater', 'created_time')
