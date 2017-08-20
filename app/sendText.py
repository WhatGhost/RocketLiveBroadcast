  
#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import http.client
import urllib.request, urllib.parse, urllib.error
import random
import json

host  = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

#用户名是登录用户中心->验证码短信->产品总览->APIID
account  = "C70086602" 
#密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "804cb35277c025e7582f5e92fe25b30d"

def sendText(mobile):
    '''
    向指定手机号发送短信验证码，成功返回验证码值，失败返回-1

    ========  ========  ==========================================
    参数      是否必选  描述
    ========  ========  ==========================================
    mobile      是        为发送短信的手机号地址
    ========  ========  ==========================================

    '''
    verification_code = generate_verification_code()
    message = "您的验证码是：" + verification_code + "。请不要把验证码泄露给其他人。"
    params = urllib.parse.urlencode({'account': account, 'password' : password, 'content': message, 'mobile':mobile,'format':'json' })
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    # print(response.status)
    if response.status == 200:
        return verification_code
    else:
        return -1

def generate_verification_code(len=6):
    ''' 
    随机生成6位的短信验证码，只包含数字
    
    ========  ========  ==========================================
    参数      是否必选  描述
    ========  ========  ==========================================
    len       否        验证码长度，默认为6
    ========  ========  ==========================================

     '''
    # 注意： 这里我们生成的是0-9的列表，当然你也可以指定这个list，这里很灵活
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    myslice = random.sample(code_list, len)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice)  # list to string
    return verification_code