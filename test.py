import imp


import socket
host = socket.getfqdn()    
addr = socket.gethostbyname(host)
print(f"Your ip is {addr}")