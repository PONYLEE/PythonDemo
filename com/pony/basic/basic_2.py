#! /usr/bin/python
# -*- coding: UTF-8 -*-

# Python空行
'''
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

记住：空行也是程序代码的一部分。
'''

# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys; x = 'pony'; sys.stdout.write(x+'\n')

#python2.x 换行 print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,。

x = 'a'
y = 'b'
# 换行输出
print(x)
print(y)

print('---------------')
#不换行输出
print(x,)
print(y,)

#不换行输出
print(x,y)

# Python2 与 Python3 print 不换行
# https://www.runoob.com/w3cnote/python-print-without-newline.html

# python3.x换行

print('------------python3.x换行---------------')
# 换行输出
print(x)
print(y)

print('---------------')
#不换行输出
print(x,end="")
print(y,end="")

#不换行输出
print(x,y,end="")

# python字句/代码组
#子句 clause
if True :
    print("aaaa") # 代码组
elif False :
    print("bbbbb")
else :
    print("ccccccc")

