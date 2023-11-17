#! /usr/bin/python
# -*- coding: UTF-8 -*-

Money = 2000
def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    # Money=0
    Money = Money + 1

print(Money)
AddMoney()
print(Money)

print("dir() func")
'''
dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。

返回的列表容纳了在一个模块里定义的所有模块，变量和函数。如下一个简单的实例：
'''

import pkg.runoob as rb
import math

content = dir(rb)
print(content)
print(dir(math))
print(rb.__name__)#特殊字符串变量__name__指向模块的名字
print(rb.__file__)#__file__指向该模块的导入文件名

print('globals() 和 locals() 函数')


'''
根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。

如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。

如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

'''
v0 = 0
def f1():
    v1 = 1
    print(locals())
    print(globals())
    return v0+v1

f1()

print('------------------------reload() 函数-------------------------------')
'''
reload() 函数的优缺点

reload() 函数的优点包括：
可以快速地重新加载修改过的模块。
无需重新启动 Python 解释器。

reload() 函数的缺点包括：
重新加载模块时，模块的全局变量和函数的状态将丢失。
重新加载模块时，模块的类和函数将被重新定义。
重新加载模块时，模块的子模块将不会被重新加载。

reload() 函数的替代方案包括：
使用 importlib.reload() 函数。
使用 execfile() 函数。
使用 subprocess.Popen() 函数。

在使用 reload() 函数时，需要注意以下几点：
只能重新加载已经导入的模块。
重新加载模块时，模块的全局变量和函数的状态将丢失。
重新加载模块时，模块的类和函数将被重新定义。
重新加载模块时，模块的子模块将不会被重新加载。
'''

import pkg.m_1 as m1

print(m1.module_var1)
m1.module_var1 = 100 + m1.module_var1
print(m1.module_var1)
print(m1.module_func())
# c1 = m1.Class1(2)
# print(c1)

from importlib import reload
reload(m1)
print(m1.module_var1)
print(m1.module_func())
