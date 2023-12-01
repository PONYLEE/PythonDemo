#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __init__ import split_line

split_line('重命名和删除文件')

import os

# os.rename('1.txt','2.txt')
# os.remove('3.txt')
# os.mkdir('D:\\idea_workspace\\PythonDemo\\com\\pony\\io\\file02')
print(os.getcwd())
os.rmdir('file02')