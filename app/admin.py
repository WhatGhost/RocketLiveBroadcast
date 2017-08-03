from django.contrib import admin

from .models import Room,LiveRoom,VideoRoom,AllSilent,OneSilent,ChatHistory,VisitHistory

admin.site.register(Room)
admin.site.register(LiveRoom)
admin.site.register(VideoRoom)
admin.site.register(AllSilent)
admin.site.register(OneSilent)
admin.site.register(ChatHistory)
admin.site.register(VisitHistory)
# Register your models here.
