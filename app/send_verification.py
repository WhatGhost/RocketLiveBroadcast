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
    # 输入Email地址和口令:
    from_addr = 'HJDLive@163.com'
    password = 'huojiandui666'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.163.com'
    #verification_code = generate_verification_code()

    msg = MIMEText(message + ' \n ', mode, encode)
    msg['From'] = _format_addr('火箭队 <%s>' % from_addr)
    msg['To'] = _format_addr('用户 <%s>' % to_addr)
    msg['Subject'] = Header('火箭队直播平台验证码', 'utf-8').encode()

    try:
        server = smtplib.SMTP(smtp_server, 25, None, 5)  # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
    except Exception as err:
        print(err)
        return 1

    server.quit()
    return 0