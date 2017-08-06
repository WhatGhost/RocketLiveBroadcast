from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route
from .models import Room, MyUser, MyUserManager, LiveRoom
from .serializers import RoomSerializer, UserSerializer, LiveRoomSerializer


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
