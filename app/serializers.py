from .models import Room, MyUser, LiveRoom, Slide, History
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
                  'active_mode',
                  )
        read_only_fields = ('id',
                            'room_name',
                            'room_introduction',
                            'room_img',
                            'room_creater',
                            'active_mode',
                            )


class HistorySerializer(serializers.ModelSerializer):
    room_creater = UserSerializer()

    class Meta:
        model = History
        fields = ('room_id',
                  'room_name',
                  'room_introduction',
                  'room_img',
                  'room_creater',
                  'history_source'
                  )
        read_only_fields = ('room_id',
                            'room_name',
                            'room_introduction',
                            'room_img',
                            'room_creater',
                            'history_source'
                            )


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ('converted_pdf',)

class LiveRoomIdSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
