import socket
import struct

def NRZ(val):
    retVal = [];
    for char in val:
        if char == '0':
            retVal.append((0,0))
        elif char == '1':
            retVal.append((1,1))
    return retVal

def Man(val):
    retVal = []
    for char in val:
        if char == '0':
            retVal.append((0,1))
        elif char == '1':
            retVal.append((1,0))
    return retVal

def RZ(val):
    retVal = []
    for char in val:
        if char == '0':
            retVal.append((0,0))
        elif char == '1':
            retVal.append((1,0))
    return retVal

def DiffMan(val):
    retVal = []
    start = '1'
    init = True
    for char in val:
        if char == '0':
            if start == '1':
                first = '0'
                second = '1'
            else:
                first = '1'
                second = '0'
                start = second
        else:
            first = start
            if first == '1':
                second = '0'
                start = second
            else:
                second = '1'
                start = second
        retVal.append((int(first),int(second)))
    return retVal

port = 10012

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost',port)
print(port)
sock.bind(server_address)

sock.listen(5)

packer2 = struct.Struct('I I')
try:
    conn, address = sock.accept()
    print("Client connected")
    #get init data
    data = conn.recv(packer2.size)
    len_code,len_val = packer2.unpack(data)
    print("Init message recieved")

    packer = struct.Struct('%ds %ds' % (len_code,len_val))
    
    data = conn.recv(packer.size)
    print("Message recieved")
    l = []
    code,val = packer.unpack(data)
    if code == "NRZ-L":
        l = NRZ(val)
    elif code == "Manchester":
        l = Man(val)
    elif code == "DiffManchester":
        l = DiffMan(val)
    elif code == "RZ":
        l = RZ(val)
    #send to client encoded message
    for el in l:
        s = packer2.pack(*el)
        conn.send(s)
finally:
    print("Connection closed")
    conn.close()
    sock.close()
    print("Socket closed")
