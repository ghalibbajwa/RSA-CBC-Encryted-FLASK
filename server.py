from email import message
import imp
import socket
import sys
import time
import main
import os

## end of imports ###
 
### init ###
 
def do(): 
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = os.environ.get('ip')
    port = 9090
    s.bind((host,port))
    s.listen(1)
    conn, addr = s.accept()
    conn.send('Connected to server'.encode())
   
    incoming_message = conn.recv(999999)
    incoming_message = incoming_message.decode()
    if(incoming_message != ''):
        main.put_session(incoming_message)
   