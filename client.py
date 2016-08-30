import socket


if __name__ == '__main__':  
    import socket  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.connect(('localhost', 8001))  
    import time  
    time.sleep(2)  
    sock.send('1')  
    print( sock.recv(1024)  )
    sock.close()  
'''
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',1080))

print(s.rev(1024).decode('utf-8'))

for data in [b'Michael',b'Tracy',b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

'''
