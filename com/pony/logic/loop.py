#! /usr/bin/python
# coding=utf-8

from __future__ import print_function
from __init__ import split_line

split_line('while')
cnt = 0
while (cnt<3):
    print('cnt is : ',cnt)
    cnt+=1

split_line('for')
for letter in "Python":
    print("current word: %s" % letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print ('当前水果: %s'% fruit)

for num in range(10,15):
    print("num = %d" %num)

split_line('break')
for num in range(10,15):
    if num==13:
        break
    print("num = %d" %num)

split_line('continue')
for num in range(10,15):
    if num==13:
        continue
    print("num = %d" %num)

split_line('pass')
for num in range(10,15):
    if num==13:
        pass
        print('This is a pass module')
    print("num = %d" %num)