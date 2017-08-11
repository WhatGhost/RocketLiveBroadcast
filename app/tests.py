from django.test import TestCase
from django.test import Client
from django.db import models
from .views import LiveRoomViewSet, UserViewSet
from .models import Room, MyUser, MyUserManager, LiveRoom, VertifyRegister
from .views import index
from .send_verification import sendMail

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


class TestLogin(TestCase):

    def setUp(self):
        print("=====Test Login")
        myuser = MyUser.objects.create(
            account='123', nickname='gyybaba', is_student='True', is_active='True', is_admin='False')
        myuser.set_password(111)
        myuser.save()

    def test_login(self):
        response = self.client.post(
            '/users/login_users/', {'account': '123', 'password': '111'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['account'],'123')
    
    def test_login_false(self):
        response = self.client.post(
            '/users/login_users/', {'account': '123', 'password': '5657'})
        self.assertFalse(response.status_code == 200)

    def tearDown(self):
        pass

class TestSendVerificaiton(TestCase):

    def setUp(self):
        print("=====Test Send Verification")

    def test_send(self):
        verificaiton = sendMail('hjdlive@sina.com')
        self.assertRegex(verificaiton,'^\w{6}$')
     
    def tearDown(self):
        pass

class TestRegister(TestCase):

    def setUp(self):
        print("=====Test Register")
        MyUser.objects.filter(account='test@test.com').delete()
        VertifyRegister.objects.filter(account='test@test.com').delete()
        VertifyRegister.objects.create(account='test@test.com',vertifycode='testve')


    def test_register(self):
        response = self.client.post(
            '/users/', {
                'account': 'test@test.com', 
                'password': 'testtest',
                'nickname': 'gyy',
                'is_student': True,
                'vertificateCode': 'testve'
                })
        self.assertEqual(response.status_code, 200)

     
    def test_register_false_with_wrongverificaiton(self):
        response = self.client.post(
            '/users/', {
                'account': 'test@test.com', 
                'password': 'testtest',
                'nickname': 'gyy',
                'is_student': True,
                'vertificateCode': 'wrongv'
                })
        self.assertFalse(response.status_code == 200)


    def tearDown(self):
        pass