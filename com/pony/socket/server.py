#! /usr/bin/python
# -*- coding: UTF-8 -*-
# server.py

import socket

s = socket.socket()
host = socket.gethostname();
port = 12345
s.bind((host,port))

s.listen(5)

while True:
    c,addr = s.accept()
    print('链接地址：', addr)
    str = 'welcome pony dome!'
    c.send(str.encode())
    c.close()

