from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, api_view
from .models import Room, MyUser, MyUserManager, LiveRoom, VertifyRegister, VertifyForgetpasswd, Slide, History
from .serializers import RoomSerializer, LiveRoomSerializer, UserSerializer, LiveRoomIdSerializer, SlideSerializer, HistorySerializer
from .send_verification import sendMail
import json
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from .utils.slide_convert import convert_and_download
from .sendText import sendText
import base64
from django.core.files.base import ContentFile


from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening



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
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = LiveRoom.objects.all()
    serializer_class = LiveRoomSerializer

    # @api_view(['POST'])
    def create(self, request):
        if not request.user.is_authenticated():
            return Response("您未登录", status=400)
        if request.user.is_student:
            return Response("您不是教师，没有创建房间的权限", status=400)
        data = request.data['file-upload']
        format, imgstr = data.split(';base64,') 
        ext = format.split('/')[-1] 
        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        r = LiveRoom(
            room_name=request.data["room-name"],
            room_introduction=request.data["room-introduction"],
            room_img=data,
            room_creater=request.user
        )
        r.save()
        serializer = LiveRoomIdSerializer(r)
        return Response(serializer.data)
    
    @list_route(methods=['patch'])
    def start_live(self, request):
        print('start live')
        roomInfo = request.data
        print(roomInfo)
        room = LiveRoom.objects.get(id=roomInfo['roomId'])
        print(room)
        if room.active_mode == 'CLOSE':
            return Response({'detail': "房间已关闭，若要开始直播请新建房间"}, status=422)
        if room.active_mode == 'START':
            return Response({'detail': "直播已经开始"}, status=422)
        room.active_mode = 'START'
        room.save()
        return Response({'detail': "开始直播成功"}, status=200)

    @list_route(methods=['patch'])
    def stop_live(self, request):
        print('stop live')
        roomInfo = request.data
        print(roomInfo)
        room = LiveRoom.objects.get(id=roomInfo['roomId'])
        print(room)
        if room.active_mode == 'CLOSE':
            return Response({'detail': "房间已关闭"}, status=422)
        if room.active_mode == 'READY':
            return Response({'detail': "直播未开始"}, status=422)
        room.active_mode = 'CLOSE'
        room.save()
        History.objects.create(
            room_id = room.id,
            room_name = room.room_name,
            room_introduction = room.room_introduction,
            room_img = room.room_img,
            room_creater = room.room_creater
        )
        return Response({'detail': "结束直播成功"}, status=200)


class HistoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
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
            return Response({'detail' :'注册成功'},status=200)
        else:
            return Response({'detail' :'验证码错误'}, status=422)
    # @ensure_csrf_cookie
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
        if(request.data.get('type')=='phone'):
            print('phone')
            vertification = sendText(account)
        else:
            print('email')
            vertification = sendMail(account)

        if vertification != -1 :
            if(request.data.get('mode') == 'register'):
                VertifyRegister.objects.create(
                    account=account, vertifycode=vertification)
                return Response({'detail': '发送验证码成功'}, status=200)
            elif request.data.get('mode') == 'forget':
                VertifyForgetpasswd.objects.create(account = account, vertifycode = vertification)
                return Response({'detail': '发送验证码成功'}, status=200)
        else:
            return Response({'detail': '发送验证码失败'}, status=422)

    # @method_decorator(csrf_protect)
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
                'is_teacher': not user.is_student,
                'nickname': user.nickname,
                'detail': '登录成功'
            }
            return Response(backInfo, status=200)
        else:
            print('验证失败')
            return Response({'detail': '登录失败'}, status=422)

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
                return Response({'detail': '更改密码成功'}, status=200)
            else:
                return Response({'detail': '原密码错误'},status=422)
        else:
            user=MyUser.objects.get(account=info['account'])
            user.nickname=info['nickname']
            user.save()
            return Response({'detail': '更改昵称成功'},status=200)

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
            return Response({'detail': '重置密码成功'}, status=200)
        else:
            return Response({'detail': '重置密码失败'}, status=422)

    @list_route(methods=['post'])
    def logout_user(self,request):
        user = request.user
        print(user)
        if request.user.is_authenticated():
            auth.logout(request)
            return Response({'detail': '登出成功'},status=200)
        else:
            return Response({'detail': '请先登录'}, status=422)


class SlideViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer

    def create(self, request):
        room = LiveRoom.objects.get(id=request.data['roomId'])
        s = Slide(
            live_room=room,
            room_slide=request.FILES['slide']
        )
        s.save()
        return Response(s.id)

    @list_route(methods=['patch'])
    def get_pdf(self, request):
        print('sending pdf...')
        s = Slide.objects.filter(live_room__id=request.data['roomId'])
        if not s.exists():
            return Response('no pdf')
        s = Slide.objects.filter(live_room__id=request.data['roomId'])[0]
        serializer = SlideSerializer(s)
        return Response(serializer.data)

    @list_route(methods=['patch'])
    def convert(self, request):
        print('start converting...')
        # get the first pdf of the same room
        s = Slide.objects.filter(live_room__id=request.data['roomId'])[0]
        try:
            pdf_name = convert_and_download(s.room_slide)
            s.converted_pdf.name = pdf_name
            print('got pdf...')
            s.save()
            serializer = SlideSerializer(s)
        except Exception:
            s.delete()
        return Response(serializer.data)



