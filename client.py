import socket
import collector
import time
import os

IP = 'localhost'

sock = socket.socket()

sock.connect((IP, 7777))

while True:
    sock.recv(16)
    name = collector.collector()
    f = open(name, "r")
    buffer = ""
    for line in f.readlines():
        buffer += line
    sock.send(buffer.encode('utf-8'))
    print("---Data send---")
    f.close()
    os.remove(name)