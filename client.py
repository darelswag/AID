#!/usr/bin/env python

import socket

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))
count = 6
socket.send("\nHey my name is Darel!\n".encode())

socket.send("\nTesting the client API\n".encode())

print("Close")
socket.close()