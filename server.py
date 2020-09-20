#import content, packages
import socket
import sys
import time

# initialisation section
# init

s = socket.socket()
host = socket.gethostname()
print('server will start on host :', host)
port = 8080
s.bind((host, port))
print("")
print("Server Done Binding to Host and Port Successfully.")
print("")
print("Server is Waiting for Incoming Connections..")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, "Has Connected to the Server and is Now Online..")
print("")

while 1:
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)
    print("Message Has Been Sent.")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print(" Client :", incoming_message)
    print("")
