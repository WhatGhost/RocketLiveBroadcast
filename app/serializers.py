from .models import  MyUser, LiveRoom, Slide, History
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('account', 'nickname', 'is_student')
        read_only_fields = ('account', 'nickname', 'is_student')


class LiveRoomSerializer(serializers.ModelSerializer):
    room_creator = UserSerializer()

    class Meta:
        model = LiveRoom
        fields = ('id',
                  'room_name',
                  'room_introduction',
                  'room_img',
                  'room_creator',
                  'active_mode',
                  )
        read_only_fields = ('id',
                            'room_name',
                            'room_introduction',
                            'room_img',
                            'room_creator',
                            'active_mode',
                            )


class HistorySerializer(serializers.ModelSerializer):
    room_creator = UserSerializer()

    class Meta:
        model = History
        fields = ('room_id',
                  'room_name',
                  'room_introduction',
                  'room_img',
                  'room_creator',
                  'history_source'
                  )
        read_only_fields = ('room_id',
                            'room_name',
                            'room_introduction',
                            'room_img',
                            'room_creator',
                            'history_source'
                            )


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ('converted_pdf',)


class LiveRoomIdSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
