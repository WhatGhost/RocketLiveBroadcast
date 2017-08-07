from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, api_view
from .models import Room, MyUser, MyUserManager, LiveRoom
from .serializers import RoomSerializer, LiveRoomSerializer, UserSerializer, LiveRoomIdSerializer
from .send_verification import sendMail
import json
from .serializers import RoomSerializer, LiveRoomSerializer, UserSerializer


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

    # @api_view(['POST'])
    def create(self, request):
        # print(request.data)
        # print(request.FILES)
        # print(request.user)
        r = LiveRoom(
            room_name=request.data["room-name"],
            room_introduction=request.data["room-description"],
            room_img=request.FILES['file-upload'],
            room_creater=MyUser.objects.all()[0]
        )
        r.save()
        serializer = LiveRoomIdSerializer(r)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        print(request.account)
        MyUserManager.create_user(
            request.account, request.nickname, request.is_student, request.password)
        return HttpResponse(status=200)
    #@list_route(methods=['post'])
    # def register_user(self,request):
        # MyUser.create_user(request.useremail, request.usernickname, True,request.password)
        # return HttpResponse(status=200)
    @list_route(methods=['patch'])
    def login_user(self, request):
        info = json.loads(str(request.body, encoding = 'utf-8'))
        account = info['account']
        user = MyUser.objects.get(account=account)
        password = info['password']
        if user.password == password:
            auth.login(request, user)
            return HttpResponse(status=200)

    @list_route(methods=['post'])
    def sendVertificateCode(self, request):
        account = json.loads(str(request.body, encoding='utf-8'))['account']
        print(account)
        vertificate = sendMail(account)
        if(vertificate != -1):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
