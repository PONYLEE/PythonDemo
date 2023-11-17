#! /usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function
from __init__ import split_line

split_line('Python算术运算符')
print(10 ** 2)  # 返回x的y次幂

# 注意：Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可。
print(9 / 2)  # x除以y
print(-9 / 2)

print(9 // 2)  # 取整除 - 返回商的整数部分（向下取整）
print(-9 // 2)

split_line('Python比较运算符')
a = 21
b = 10
c = 0

if  a == b :
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

