from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from app import views

router = routers.SimpleRouter()
router.register(r'rooms', views.RoomViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^', include(router.urls))
]
