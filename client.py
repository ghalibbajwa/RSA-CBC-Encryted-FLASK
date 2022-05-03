import socket
import sys
import time
 
def do(message):
    s = socket.socket()
    host = 'Ghalib'
    port = 8080
    s.connect((host,port))
    print(" Connected to chat server")
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print(" Server : ", incoming_message)
    print("")
    message = message.encode()
    s.send(message)
    print("message has been sent...")
    print("")