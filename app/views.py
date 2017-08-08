from django.shortcuts import render,get_object_or_404
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, api_view
from .models import Room, MyUser, MyUserManager, LiveRoom, VertifyRegister
from .serializers import RoomSerializer, LiveRoomSerializer, UserSerializer, LiveRoomIdSerializer
from .send_verification import sendMail
import json
from .serializers import RoomSerializer, LiveRoomSerializer, UserSerializer
from datetime import datetime,timedelta

def index(request):
    return render(request, 'index.html')


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @list_route(methods=['delete'])
    def clear_rooms(self,request):
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
            room_introduction=request.data["room-introduction"],
            room_img=request.FILES['file-upload'],
            room_creater=MyUser.objects.all()[0]
        )
        r.save()
        serializer = LiveRoomIdSerializer(r)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset=MyUser.objects.all()
    serializer_class=UserSerializer

    def create(self,request):
        info=json.loads(str(request.body,encoding='utf-8'))
        endTime = datetime.now()
        startTime = endTime- timedelta(minutes = -30)
        userSets = VertifyRegister.objects.filter(account=info['account'],vertifycode=info['vertificateCode'])
        if userSets.exists():
            print(endTime-userSets[0].vertifytime < timedelta(minutes = 30))
            MyUser.objects.create_user(info['account'],info['nickname'],info['is_student'])
            return HttpResponse(status=200)
        else:
            return Response('验证码不存在',status=422)
    

    @list_route(methods=['post'])
    def sendVertificateCode(self, request):
        account = json.loads(str(request.body, encoding='utf-8'))['account']
        print(account)
        vertification = sendMail(account)
        if(vertification != -1):
            VertifyRegister.objects.create(account=account, vertifycode=vertification)
            return HttpResponse(status=200)           
        else:
            return HttpResponse(status=422)



    @list_route(methods=['post'])
    def login_users(self,request):
        info=json.loads(str(request.body,encoding='utf-8'))
        account=info['account']
        print(account)
        user=MyUser.objects.get(account=account)
        print(user.password)
        if True:
            auth.login(request,user)
            return Response(info['account'],status=200)
        else:
            print('sb')
            return HttpResponse(status=200)
    @list_route(methods=['patch'])
    def change_info(self,request):
        info=json.loads(str(request.body,encoding='utf-8'))
        choose=info['is_password']
        user=MyUser.objects.get(account=info['account'])
        if choose==True:
            return HttpResponse(status=200)
        else:
            user.nickname=info['nickname']
            user.save()
            return HttpResponse(status=200)

        
        