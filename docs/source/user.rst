用户系统API
===========

class **UserViewSet(viewsets.ModelViewSet)**

| 该类继承自viewsets.ModelViewSet类，包含了用户系统的各种函数

**方法：**

| **create(self, request)**

-  用户系统注册函数,重写其自带的create函数
-  request中包含前端传入的账户密码等数据，其中前端传入的密码为经过SHA256算法加密后的值。
-  此函数会查询验证码的正确性，验证码正确则注册成功返回状态码200；不成功返回失败状态码。

| **current\_user(self,request)** 

-  返回当前用户信息 
-  若为匿名用户各字段返回空值，否则返回当前用户的账户，昵称，是否是教师等信息

| **sendVertificateCode(self, request)** 

-  发送验证码函数，用户注册与忘记密码功能 
-  根据传入request的type字段进行判断，向传入的account字段发送相应验证码

| **login\_users(self, request)** 

-  用户登录函数 
-  使用django自带用户系统的登录函数，根据传入的用户名与密码(SHA256加密后值)进行登录校验
-  成功则返回用户信息，失败返回失败状态码

| **change\_info(self,request)** 

-  修改用户信息(昵称，密码)函数 
-  进行判断是修改昵称还是修改密码，进行相应的修改

| **forget\_info(self,request)** 

-  用户忘记密码函数 
-  检验验证码正确性，若正确则重新设置密码，否则返回更改失败

| **logout\_user(self,request)** 

-  用户登出函数 
-  检验是否已经登录，若已经登录，使其登出，返回登出成功，否则返回请先登录
