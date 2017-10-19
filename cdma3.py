import socket
import select
import os
import sys
port = 10001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost',port)
userid = str(os.getpid())
sock.connect(server_address)
sock.sendall(userid)
print userid
socket_list = [sock]
while True:
    inputs, outputs, errors = select.select(socket_list , [], [], 1)
    for s in inputs:
        if s is sock:
            data = s.recv(20)
            print(data)
            if data == "NNNN":
                sock.close()
                sys.exit()
