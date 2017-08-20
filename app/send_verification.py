from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import random
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendMail(to_addr, message="您的验证码为： ", mode='plain', encode='utf-8'):
    '''
    向to_addr指定的邮件地址发送验证码邮件，若发送成功返回验证码，不成功返回-1

    ========  ========  ==========================================
    参数      是否必选  描述
    ========  ========  ==========================================
    to_addr   是        发送邮件的地址

    message   否        邮件内容，默认为“您的验证码为： ”

    mode      否        发送文本模式，默认为plain

    encode    否        编码方式，默认为utf-8
    ========  ========  ==========================================

 
    '''
    # 输入Email地址和口令:
    from_addr = 'HJDLive@163.com'
    password = 'huojiandui666'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.163.com'
    verification_code = generate_verification_code()

    msg = MIMEText(message + ' \n ' + verification_code, mode, encode)
    msg['From'] = _format_addr('火箭队 <%s>' % from_addr)
    msg['To'] = _format_addr('用户 <%s>' % to_addr)
    msg['Subject'] = Header('火箭队直播平台验证码', 'utf-8').encode()

    try:
        server = smtplib.SMTP(smtp_server, 25, None, 10)  # SMTP协议默认端口是25
        server.set_debuglevel(0)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
    except Exception as err:
        print(err)
        return -1

    server.quit()
    return verification_code


def generate_verification_code(len=6):
    ''' 
    随机生成六位邮箱验证码，包含数字字母
    
    ========  ========  ==========================================
    参数      是否必选  描述
    ========  ========  ==========================================
    len       否        验证码长度，默认为6
    ========  ========  ==========================================

    '''
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91):  # 对应从“A”到“Z”的ASCII码
        code_list.append(chr(i))
    for i in range(97, 123):  # 对应从“a”到“z”的ASCII码
        code_list.append(chr(i))

    myslice = random.sample(code_list, len)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice)  # list to string
    return verification_code
