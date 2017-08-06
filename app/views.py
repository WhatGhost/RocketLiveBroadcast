from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from .models import Room, MyUser, MyUserManager, LiveRoom
from .serializers import RoomSerializer, UserSerializer, LiveRoomSerializer
import json


def index(request):
    return render(request, 'index.html')


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @list_route(methods=['delete'])
    def clear_rooms(self, request):
        rooms = Room.objects.all()
        rooms.delete()
        return HttpResponse(status=200)


class LiveRoomViewSet(viewsets.ModelViewSet):
    queryset = LiveRoom.objects.all()
    serializer_class = LiveRoomSerializer

    def create(self, request):
        new_room = self.get_serializer(data=request.data)
        new_room.is_valid()
        print(new_room.errors)
        # if LiveRoom.objects.all():
        #     new_room['room_id'] = LiveRoom.objects.all(
        #     ).aggregate(Max("room_id"))
        # else:
        #     new_room['room_id'] = 1
        
        if new_room.is_valid():
            new_room.save()
            return Response(new_room.data, status=200)
        else:
            return HttpResponse(400)


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        MyUserManager.create_user(
            request.account, request.nickname, request.is_student, request.password)
        return HttpResponse(status=200)
    #@list_route(methods=['post'])
    # def register_user(self,request):
        #MyUser.create_user(request.useremail, request.usernickname, True,request.password)
        # return HttpResponse(status=200)

    def get(self, request):
        account = request.account
        user = get_object_or_404(queryset, account=account)
        password = user.password
        if user.password == request.password:
            auth.login(request, user)
            return HttpResponse(status=200)
