from django.test import TestCase
from django.test import Client
from django.db import models
from .views import LiveRoomViewSet,UserViewSet
from .models import Room, MyUser, MyUserManager, LiveRoom, VertifyRegister
from .views import index


# Create your tests here.
class TestView(TestCase):
    """Test the views of the application"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class TestCreateRoom(TestCase):

    def setUp(self):
        print("=====in setup")
        myuser=MyUser.objects.create(account='123',nickname='gyy',is_student='True',is_active='True',is_admin='False')
        myuser.set_password(111)
        myuser.save()

    def test_create_room(self):
        response = self.client.post('/users/login_users/',{'account': '123', 'password': '111'})
        self.assertEqual(response.status_code , 200)

    def tearDown(self):
        pass