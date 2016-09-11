from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
def _format_addr(s):
       name,addr = parseaddr(s)
       #print(name)
       #print(addr)
       return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input('From.. ')
password = input('Password.. ')
to_addr = input('To.. ')
smtp_server = input('Smtp server.. ')


msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者<%s>'  % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来着SMTP的问候..','utf-8').encode()

#邮件正文是MIMEText:
#msg.attach(MIMEText('send with file...','plain','utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>'+'<p><img src="cid:0"></p>'+'</body></html>','html','utf-8'))
#添加附件就是加上一个MIMEBase，从本地读取一个图片
with open ('tong.png','rb') as f:
        mime = MIMEBase('image','png',filename='tong.png')
        mime.add_header('content-Disposition','attachment',filename='tong.png')
        mime.add_header('Content-ID','<0>')
        mime.add_header('X-Attachment-Id','0')
        
        mime.set_payload(f.read())
        encoders.encode_base64(mime)

        msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server,465)
#打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
#登入邮件
server.login(from_addr,password)
#发送邮件，内容为msg转成的msg
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()



'''
#-------------------------------------------v3.0-----------------------------
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
def _format_addr(s):
       name,addr = parseaddr(s)
       #print(name)
       #print(addr)
       return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input('From.. ')
password = input('Password.. ')
to_addr = input('To.. ')
smtp_server = input('Smtp server.. ')


msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者<%s>'  % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来着SMTP的问候..','utf-8').encode()

#邮件正文是MIMEText:
msg.attach(MIMEText('send with file...','plain','utf-8'))

#添加附件就是加上一个MIMEBase，从本地读取一个图片
with open ('tong.png','rb') as f:
	mime = MIMEBase('image','png',filename='tong.png')
	mime.add_header('content-Disposition','attachment',filename='tong.png')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')
	
	mime.set_payload(f.read())
	encoders.encode_base64(mime)

	msg.attach(mime)


server = smtplib.SMTP_SSL(smtp_server,465)
#打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
#登入邮件
server.login(from_addr,password)
#发送邮件，内容为msg转成的msg
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()

#......................................v3.0------------------------------------

'''
'''
#------------------------------v2.0------------------------
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib
#def _format_addr(s):
#	name,addr = parseaddr(s)
#	print(name)
#	print(addr)
#	return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input('From.. ')
password = input('Password.. ')
to_addr = input('To.. ')
smtp_server = input('Smtp server.. ')

#msg = MIMEText('hello,send by python..','plain','utf-8')
msg = MIMEText('<html><body><h1>Hello</h1>'+'<p>send by <a href="http://www.python.org">Python</a>...</p>' +'</body></html>','html','utf-8')
#msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['From'] = Header(from_addr,'utf-8')
#msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['To'] = Header(to_addr,'utf-8')
msg['subject'] = Header('来着SMTP的问候...','utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server,465)
#打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
#登入邮件
server.login(from_addr,password)
#发送邮件，内容为msg转成的msg
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()

#--------------------------------v2.0---------------------







#-------------------v1.0-------------------------
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
#----------------------------v1.0----------------------
'''
