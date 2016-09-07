#from email.mime.text import MIMEText
#注意：不能将文件名叫做email.py，否则会报 ImportError: No module named mime.text

from email.mime.text import MIMEText
msg = MIMEText('hello,send by python..','plain','utf-8')

#发送人的邮件和密码
from_addr = input('From.. ')
password = input('Password.. ')
#收件人的邮件
to_addr = input('To.. ')


smtp_server = input('SMTP server: ')

import smtplib
#smtp服务器授权
server = smtplib.SMTP_SSL(smtp_server,465)
#打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
#登入邮件
server.login(from_addr,password)
#发送邮件，内容为msg转成的msg
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
