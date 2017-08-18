from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from app import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register(r'rooms', views.RoomViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'liveroom', views.LiveRoomViewSet)
router.register(r'slide', views.SlideViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
