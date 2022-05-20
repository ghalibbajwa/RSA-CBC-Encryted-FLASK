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
    host = os.environ.get('ip')
    port = 9091
    s.bind((host,port))
    s.listen(1)
    conn, addr = s.accept()
    conn.send('Connected to server'.encode())
   
    incoming_message = conn.recv(999999)
    incoming_message = incoming_message.decode()
    if(incoming_message != ''):
        main.put_session(incoming_message)
   