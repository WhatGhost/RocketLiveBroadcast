from django.shortcuts import render,get_object_or_404
from django.contrib import auth
import json
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route
from .models import Room,MyUser,MyUserManager
from .serializers import RoomSerializer,UserSerializer
# Create your views here.
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


class UserViewSet(viewsets.ModelViewSet):
    queryset=MyUser.objects.all()
    serializer_class=UserSerializer

    def create(self,request):
        info=json.loads(str(request.body,encoding='utf-8'))
        MyUser.objects.create_user(info['account'],info['nickname'],info['is_student'])
        return HttpResponse(status=200)
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

        
        