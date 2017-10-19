import socket
import struct

port = 10012

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost',port)

sock.connect(server_address)
print("connected to server")
#packer = struct.Struct('5s 4s')
packer2 = struct.Struct('I I')
try:
    #code,val = ("NRZ-L","1100")
    code,val = ("DiffManchester","10110001101")
    init = (len(code),len(val))
    init = packer2.pack(*init)
    sock.sendall(init)
    packer = struct.Struct('%ds %ds' % (len(code),len(val)))
    msg = (code,val)
    msg = packer.pack(*msg)
    sock.sendall(msg)
    #print(len(code)-1)
    for i in range(len(val)):
        msg = sock.recv(packer2.size)
        msg = packer2.unpack(msg)
        print(msg)
finally:
    sock.close()
