#!/usr/bin/python
# coding=utf-8
from __future__ import print_function
from __init__ import split_line
split_line('try-except-else 语句')

try:
    fh = open('11.txt', 'r')
    fh.write('this a test file!')
# except:# 不带任何异常类型使用except，它捕获所有的异常。
except(IOError, NameError):  # 使用except而带多种异常类型
    print('Error: 没有找到文件或读取文件失败')
else:
    print('内容写入文件成功')
    fh.close()

print('done!')

split_line('try-finally-execept 语句')
try:
    fh = open("2.txt", "r")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print("关闭文件")
        fh.close()
except (IOError):
    print("Error: IOERROR")

split_line('异常的参数')

def func1(var):
    try:
        return int(var)
    except ValueError as args:
        print("参数没有包含数字\n", args)

print(func1("10z"))

split_line('触发异常')

def my_except(level):
    if level <1:
        raise Exception("Invalid level!",level) # 触发异常后，后面的代码就不会再执行
    return level

try:
    print(my_except(-1))
except Exception as args:
    print(1,args)
else:
    print(2)

split_line('用户自定义异常')

class NetWorkerError(RuntimeError): #继承自RuntimeError
    def __init__(self,args):
        self.args=args

    def __str__(self):
        # return str(self.args)
        return ''.join(self.args)


try:
    raise NetWorkerError("Bad hostname")
except NetWorkerError as e:
    print(e)