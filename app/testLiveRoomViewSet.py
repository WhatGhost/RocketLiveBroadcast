from django.test import TestCase
from django.test import Client
from django.db import models
from .views import LiveRoomViewSet, UserViewSet
from .models import Room, MyUser, MyUserManager, LiveRoom, VertifyRegister, VertifyForgetpasswd
from .views import index

class TestCreate(TestCase):

    def setUp(self):
        print("=====Test Create Room")
        myuser1 = MyUser.objects.create(
            account='teacher@t.com', nickname='gyybaba', is_student='False', is_active='True', is_admin='True')
        myuser1.set_password('teacher')
        myuser1.save()
        myuser2 = MyUser.objects.create(
            account='student@s.com', nickname='gyybaba', is_student='True', is_active='True', is_admin='False')
        myuser2.set_password('student')
        myuser2.save()

    def test_create(self):
        response = self.client.post('/liveroom/')
        self.assertEqual(response.data['detail'], '您未登录')

    def test_create_with_student(self):
        self.assertTrue(self.client.login(
            account='student@s.com', password='student'))
        response = self.client.post('/liveroom/')
        self.assertEqual(response.data['detail'], '您不是教师，没有创建房间的权限')
    
    #却创建房间测试，文件传入出问题

    # def test_create_with_teacher(self):
    #     self.assertTrue(self.client.login(account='teacher@t.com', password='teacher'))
    #     response = self.client.post(
    #         '/liveroom/', {'room-name': 'testrooom', 'room-introduction': 'nothing', })
    #     self.assertEqual(response.data['room_nmea'], 'testrooom')

    def tearDown(self):
        pass

