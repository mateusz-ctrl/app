import socket
import sys
import time

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('server', 1234)
#print ('connecting to %s port %s' % server_address)
mysocket.connect(server_address)
start = time.time()
try:  
    while True: 
        message = b'message'
        #print ('sending "%s"' % message)
        mysocket.sendall(message)
        time.sleep(3)
        #gdy chcemy odbierac potwierdzenie:
        #data = sock.recv(16)
        #print ('received "%s"' % data)
        #gdy chcemy zakonczyc po jakims czasie transmisje:
        #if time.time() > start + period_of_time : break
finally:
    print ( 'closing socket')
    mysocket.close()
