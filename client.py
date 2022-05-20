import socket
import sys
import time
 
def do(message,host):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = host
    port = 9090
    s.connect((host,port))
    print(" Connected to chat server")
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
   
    message = message.encode()
    s.send(message)
    s.close()