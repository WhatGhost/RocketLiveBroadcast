from .models import Room, MyUser
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
