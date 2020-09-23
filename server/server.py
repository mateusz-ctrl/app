import socket
import sys
import time

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 1234)
print ( "starting up on %s port %s" % server_address)
mysocket.bind(server_address)
mysocket.listen(1)

while True:
    print ( "waiting for a connection")
    connection, client_address = mysocket.accept()
    try:
        #print ( "connection from", client_address)
        while True:
            data = connection.recv(16)
            print ( 'received "%s"' % data)
            #gdy chcemy wysyłać potwierdzenie odbioru:
            #if data:
              #   print ( 'sending confirmation')
              #  connection.sendall(b'confirmation')
           # else:
            #   print ( 'no data from', client_address)
            #   break
    finally:
        connection.close()
