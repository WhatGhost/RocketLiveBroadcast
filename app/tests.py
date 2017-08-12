from django.test import TestCase
from django.test import Client
from django.db import models
from .views import LiveRoomViewSet, UserViewSet
from .models import Room, MyUser, MyUserManager, LiveRoom, VertifyRegister, VertifyForgetpasswd
from .views import index
from .send_verification import sendMail

# Create your tests here.

# 测试访问主页


class TestView(TestCase):
    """Test the views of the application"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# 测试登录


class TestLogin(TestCase):

    def setUp(self):
        print("=====Test Login")
        myuser = MyUser.objects.create(
            account='123', nickname='gyybaba', is_student='True', is_active='True', is_admin='False')
        myuser.set_password(111)
        myuser.save()

    # 正确密码登录
    def test_login(self):
        response = self.client.post(
            '/users/login_users/', {'account': '123', 'password': '111'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['account'], '123')

    # 错误密码登录
    def testLoginWithWrongPassword(self):
        response = self.client.post(
            '/users/login_users/', {'account': '123', 'password': '5657'})
        self.assertFalse(response.status_code == 200)

    # 错误用户名登录
    def testLoginWithWrongAccount(self):
        response = self.client.post(
            '/users/login_users/', {'account': 'gao', 'password': '111'})
        self.assertFalse(response.status_code == 200)

    def tearDown(self):
        pass


# 测试发送验证码
class TestSendVerificaiton(TestCase):

    def setUp(self):
        print("=====Test Send Verification")

    def test_send(self):
        verificaiton = sendMail('hjdlive@sina.com')
        self.assertRegex(verificaiton, '^\w{6}$')

    def test_send_with_wrong_email(self):
        verificaiton = sendMail('111')
        self.assertEqual(verificaiton, -1)

    def tearDown(self):
        pass


# 测试注册
class TestRegister(TestCase):

    def setUp(self):
        print("=====Test Register")
        MyUser.objects.filter(account='test@test.com').delete()
        VertifyRegister.objects.filter(account='test@test.com').delete()
        VertifyRegister.objects.create(
            account='test@test.com', vertifycode='testve')

    # 测试注册
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
        self.assertTrue(MyUser.objects.filter(
            account='test@test.com', nickname='gyy').exists())

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


class TestCurrentUser(TestCase):
    def setUp(self):
        print("======Test get current user")
        myuser = MyUser.objects.create(
            account='123', nickname='gyybaba', is_student='True', is_active='True', is_admin='False')
        myuser.set_password(111)
        myuser.save()

    def test_Create_without_login(self):
        response = self.client.post('/users/current_user/')
        self.assertEqual(response.data['account'], None)

    def test_Create_with_login(self):
        login = self.client.post(
            '/users/login_users/', {'account': '123', 'password': '111'})
        response = self.client.post('/users/current_user/')
        self.assertEqual(response.data['account'], '123')

    def tearDown(self):
        pass


class TestCurrentUser(TestCase):
    def setUp(self):
        print("======Test get current user")
        myuser = MyUser.objects.create(
            account='123', nickname='gyybaba', is_student='True', is_active='True', is_admin='False')
        myuser.set_password(111)
        myuser.save()

    def testCreateWithoutLogin(self):
        response = self.client.post('/users/current_user/')
        self.assertEqual(response.data['account'], None)

    def testCreateWithLogin(self):
        login = self.client.post(
            '/users/login_users/', {'account': '123', 'password': '111'})
        response = self.client.post('/users/current_user/')
        self.assertEqual(response.data['account'], '123')

    def tearDown(self):
        pass


class TestLogout(TestCase):
    def setUp(self):
        print("======Test Logout")
        myuser = MyUser.objects.create(
            account='123', nickname='gyybaba', is_student='True', is_active='True', is_admin='False')
        myuser.set_password(111)
        myuser.save()

    def test_logout(self):
        self.client.post(
            '/users/login_users/', {'account': '123', 'password': '111'})
        logout = self.client.post('/users/logout_user/')
        self.assertEqual(logout.status_code, 200)
        self.assertEqual(logout.data, '登出成功')
        currentUser = self.client.post('/users/current_user/')
        self.assertEqual(currentUser.data['account'], None)

    def test_logout_without_login(self):
        logout = self.client.post('/users/logout_user/')
        self.assertEqual(logout.data, '请先登录')

    def tearDown(self):
        pass


class TestRegisterVerification(TestCase):
    def setUp(self):
        print("=====Test Send Register Verification")

    def test_send(self):
        self.client.post(
            '/users/sendVertificateCode/', {'account': 'register@r.com', 'mode': 'register'})
        self.assertTrue(VertifyRegister.objects.filter(
            account='register@r.com').exists())

    def tearDown(self):
        pass


class TestForgetVerification(TestCase):
    def setUp(self):
        print("=====Test Send Forget Verification")

    def test_send(self):
        self.client.post(
            '/users/sendVertificateCode/', {'account': 'forget@f.com', 'mode': 'forget'})
        self.assertTrue(VertifyForgetpasswd.objects.filter(
            account='forget@f.com').exists())

    def tearDown(self):
        pass
