from .models import Room, MyUser, LiveRoom
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('text',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('account', 'nickname', 'is_student')
        read_only_fields = ('account', 'nickname', 'is_student')


class LiveRoomSerializer(serializers.ModelSerializer):
    room_creater = UserSerializer()

    class Meta:
        model = LiveRoom
        fields = ('id',
                  'room_name',
                  'room_introduction',
                  'room_img',
                  'room_creater',
                  )
        read_only_fields = ('id',
                            'room_name',
                            'room_introduction',
                            'room_img',
                            'room_creater',
                            )


class LiveRoomIdSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
