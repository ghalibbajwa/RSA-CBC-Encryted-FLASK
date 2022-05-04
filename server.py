from email import message
import imp
import socket
import sys
import time
import main
 
## end of imports ###
 
### init ###
 
def do(): 
    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host,port))
    s.listen(1)
    conn, addr = s.accept()
    conn.send('Connected to server'.encode())
   
    incoming_message = conn.recv(999999)
    incoming_message = incoming_message.decode()
    if(incoming_message != ''):
        main.put_session(incoming_message)
    
    print(" Client : ", incoming_message)
    print("")