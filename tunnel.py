import socket, _thread

ip = input('Please enter an IP or Hostname to forward traffic to that: ')
to_port = int(input('Please enter a port which you want to forward to: '))
from_port = int(input('Please enter a port which you want to forward from: '))

def do(ip_address,port, x):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port))
    while True:
        data = x.recv(1024000)
        if data == b'':
            return
        s.sendall(data)
        data2 = s.recv(1024000)
        if data2 == b'':
            return
        x.sendall(data2)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', from_port))
s.listen()
while True:
    a, b = s.accept()
    _thread.start_new_thread(do, (ip, to_port, a))

