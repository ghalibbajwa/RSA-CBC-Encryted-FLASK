from email import message
import socket
import sys
import time
 
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
    while 1:
                #message = input(str(">> "))
                #message = message.encode()
                #conn.send(message)
                #print("message has been sent...")
                #print("")
                incoming_message = conn.recv(1024)
                incoming_message = incoming_message.decode()
                print(" Client : ", incoming_message)
                print("")