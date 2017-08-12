from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, api_view
from .models import Room, MyUser, MyUserManager, LiveRoom, VertifyRegister, VertifyForgetpasswd
from .serializers import RoomSerializer, LiveRoomSerializer, UserSerializer, LiveRoomIdSerializer
from .send_verification import sendMail
import json
from .serializers import RoomSerializer, LiveRoomSerializer, UserSerializer
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator


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
            room_introduction=request.data["room-introduction"],
            room_img=request.FILES['file-upload'],
            room_creater=request.user
        )
        r.save()
        serializer = LiveRoomIdSerializer(r)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        info = request.data
        #info = json.loads(str(request.body, encoding='utf-8'))
        endTime = datetime.now()
        startTime = endTime + timedelta(minutes=-30)
        userSets = VertifyRegister.objects.filter(
            account=info['account'], vertifycode=info['vertificateCode'], vertifytime__range=(startTime,endTime))
        if userSets.exists():
            print(endTime - userSets[0].vertifytime < timedelta(minutes=30))
            MyUser.objects.create_user(
                info['account'], info['nickname'], info['is_student'], info['password'])
            return HttpResponse(status=200)
        else:
            return Response('验证码不存在', status=422)

    @list_route(methods=['post'])
    def current_user(self,request):
        user = request.user
        if request.user.is_authenticated():
            print("authenticated~")
            return Response({"account": user.account, "nickname": user.nickname, "isTeacher": not user.is_student})
        else:
            return Response({"account": None, "nickname": None, "isTeacher": False})

    @list_route(methods=['post'])
    def sendVertificateCode(self, request):
        account = request.data.get('account')
        #account = json.loads(str(request.body, encoding='utf-8'))['account']
        print(account)
        vertification = sendMail(account)
        if vertification != -1 :
            if(request.data.get('mode') == 'register'):
                VertifyRegister.objects.create(
                    account=account, vertifycode=vertification)
                return HttpResponse(status=200)
            elif request.data.get('mode') == 'forget':
                VertifyForgetpasswd.objects.create(account = account, vertifycode = vertification)
                return HttpResponse(status=200)
        else:
            return HttpResponse(status=422)

    @method_decorator(csrf_protect)
    @list_route(methods=['post'])
    def login_users(self, request):
        print(request.user)
        user = auth.authenticate(account=request.data.get('account'),
                                 password=request.data.get('password'))
        if user is not None:
            print('验证成功')
            auth.login(request, user)
            backInfo = {
                'account': request.data.get('account', ''),
                'is_student': True,
                'nickname': user.nickname
            }
            return Response(backInfo, status=200)
        else:
            print('验证失败')
            return HttpResponse(status=422)

    @list_route(methods=['patch'])
    def change_info(self,request):
        info = request.data
        #info=json.loads(str(request.body,encoding='utf-8'))
        #user=MyUser.objects.get(account=info['account'])
        print(111)
        print(info['is_password'])
        if info['is_password']:
            print(info['account'])
            print(info['oldpassword'])
            user =auth.authenticate(account=info['account'],password=info['oldpassword'])
            if user is not None :
                #user.check_password(info['password'])
                user.set_password(info['newpassword'])
                user.save()
                return HttpResponse(status=200)
            else:
                return Response('原密码错误',status=422)
        else:
            user=MyUser.objects.get(account=info['account'])
            user.nickname=info['nickname']
            user.save()
            return HttpResponse(status=200)

    @list_route(methods=['patch'])
    def forget_info(self,request):
        info = request.data
        endTime = datetime.now()
        startTime = endTime + timedelta(minutes=-30)
        print(info['account'])
        userSets = VertifyForgetpasswd.objects.filter(
            account=info['account'], vertifycode=info['vertificateCode'], vertifytime__range=(startTime,endTime))
        print(userSets)
        if userSets.exists():
            print(endTime - userSets[0].vertifytime < timedelta(minutes=30))
            user=MyUser.objects.get(account=info['account'])
            print(user.password)
            user.set_password(info['password'])
            print(user.password)
            user.save()
            return HttpResponse(status=200)
        else:
            return Response('更改失败', status=422)

    @list_route(methods=['post'])
    def logout_user(self,request):
        user = request.user
        print(user)
        if request.user.is_authenticated():
            auth.logout(request)
            return Response(status=200)
        else:
            return Response('请先登录',status=422)




