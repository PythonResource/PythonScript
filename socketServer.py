#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('连接地址: ' + str(addr))
    c.send('欢饮访问菜鸟教程')
    c.close()