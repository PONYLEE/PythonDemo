#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __init__ import split_line


split_line('file')
fo = open('1.txt','r+')
print ("文件名: ", fo.name)
print ("是否已关闭 : ", fo.closed)
print ("访问模式 : ", fo.mode)
# print ("末尾是否强制加空格 : ", fo.softspace)


split_line("read & write")
file1= open('1.txt','r+')
str = file1.read(10)
print(str)
file1.write( "abc")
print(file1.read())
file1.close()


split_line('文件定位')
file2 = open("1.txt","r+")
print(file2.tell())
file2.write( "222")
print(file2.tell())
rd = file2.read(5)
print(rd)
print(file2.tell())
file2.seek(0,0)
print(file2.read(8))
print(file2.tell())
file2.close()
