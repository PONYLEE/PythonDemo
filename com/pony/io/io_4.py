#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __init__ import split_line

split_line('file')

import sys,time
split_line('flush')
fo = open('2.txt','r+')
print(fo.name)
print(fo.fileno())
print(fo.isatty())
print(fo.readline().strip())
# print(fo.truncate(10))
fo.write('aaaaaaaaaa')
fo.writelines(['bbbbbb\n','ccccccccccc'])
fo.seek(0,0)
print(fo.readlines())
fo.flush()
fo.close()

split_line('进度条类型')
for i in range(30):
    sys.stdout.write('*')
    sys.stdout.flush()
    time.sleep(0.2) 