import socket

if __name__ == '__main__':  
    import socket  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.bind(('localhost', 8001))  
    sock.listen(5)  
    while True:  
        connection,address = sock.accept()  
        try:  
            connection.settimeout(5)  
            buf = connection.recv(1024)  
            if buf == '1':  
                connection.send('welcome to server!')  
            else:  
                connection.send('please go out!')  
        except socket.timeout:  
            print ('time out'  )
        connection.close()  



'''
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',1080))

s.listen(5)
print('Waiting for connection...')

while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

def tcplink(sock,addr):
    print('Accept new connection from %s %s..' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)


'''



'''
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('www.sina.com.cn',80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close()

header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

with open('sina.html','wb') as f:
    f.write(html)
  '''  


'''
import time 
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
       self.nameInput = Entry(self)
       self.nameInput.pack()
       #messagebox.showinfo('Message',self.nameInput.get())
       self.alertButton = Button(self,text='Hello',compound="left",command=self.hello)
       self.alertButton.pack()
       self.quitButton = Button(self,text='Quit',command=self.quit)
       self.quitButton.pack()
       
       
    def hello(self):
        
        name = self.nameInput.get()
        while (name ==''):
            messagebox.showinfo('message','please return')
            break
        while (name !=''):
            #messagebox.showinfo('ERROR','Please input the char')
            #time.sleep(5)
            messagebox.showinfo('Message','Hello,%s' %name)
            break
        #if (name == ''):
        #    messagebox.showinfo('Error','please input the char')
        
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()


'''

'''

from tkinter import *

class Application(Frame):
        def __init__(self,master=None):
            Frame.__init__(self,master)
            self.pack()
            self.createWidgets()

        def createWidgets(self):
            self.helloLabel = Label(self,text='Hello,world!')
            self.helloLabel.pack()
            self.quitButton = Button(self,text='Quit',command=self.quit)
            self.quitButton.pack()
app  = Application()

app.master.title('Hello World')

app.mainloop()
'''
