#! /usr/bin/python
# coding=utf-8

"""

Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。

Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

时间间隔是以秒为单位的浮点小数。

每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
"""

import time
from __init__ import split_line

split_line('time')
t1 = time.time()
print(t1)
t2 = time.localtime()
print(t2)
t3 = time.asctime()
print(t3)
split_line(" 格式化成2016-03-20 11:45:39形式")
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
split_line('将格式字符串转换为时间戳')
print(time.strptime('2023-11-29 16:48:46','%Y-%m-%d %H:%M:%S'))
print(time.mktime(time.strptime('2023-11-29 16:48:46','%Y-%m-%d %H:%M:%S')))
print(time.process_time())
time.sleep(1)
print(time.process_time())
print(time.timezone)

split_line('calendar')
import calendar
cal = calendar.month(2023,12)
print(cal) 
