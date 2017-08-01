from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route
from .models import Room
from .serializers import RoomSerializer
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