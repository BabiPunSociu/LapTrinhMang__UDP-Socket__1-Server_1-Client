# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:25:07 2023

@author: ADMIN
"""

import socket

if __name__ == '__main__':

    ip = "127.0.0.1"
    port = 28111
    socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    socket.bind((ip, port))
    print("waiting for client....")
    # Nhan 1
    byteAddressPair = socket.recvfrom(1024)
    messageRecv = byteAddressPair[0].decode('utf-8')
    print(messageRecv)
    address = byteAddressPair[1] # Lay dia chi Client
    # Gui 2
    socket.sendto('hello client...'.encode('utf-8'), byteAddressPair[1])
    
    while True:
        # Nhan 3
        a1 = socket.recvfrom(1024)
        message = a1[0].decode('utf-8')
        print(message)
        # Gui 4
        sendMsg = input('send client: ')
        socket.sendto(sendMsg.encode('utf-8'), address)
    socket.close()
