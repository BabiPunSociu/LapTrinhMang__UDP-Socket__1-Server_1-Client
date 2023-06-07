# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:54:12 2023

@author: ADMIN
"""

import socket

if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 28100
    socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    message = "Hello server. This is client"
    # Gui 1
    socket.sendto(str(message).encode('utf-8'), (ip, 28111))
    # Nhan 2
    msg = socket.recvfrom(1024)
    msgReal = msg[0].decode('utf-8')
    address= msg[1] # Lay dia chi Server
    print(msgReal)
    while True:
        # Gui 3
        sendServer = input('Send server: ')
        socket.sendto(sendServer.encode('utf-8'), address)
        # Nhan 4
        a = socket.recvfrom(1024)
        message = a[0].decode('utf-8')
        print(message)
        print("success")
    socket.close()
