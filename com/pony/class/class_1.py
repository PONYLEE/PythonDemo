#! /usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function
from __init__ import print_split_line


class Employee:
    '所有员工的基类'
    empCount = 0  # empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。

    def __init__(self, name, salary):  # 第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("total employee %d" % Employee.empCount)  # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。self代表类的实例，而非类

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def prt(self):
        print(self)
        print(self.__class__)


print_split_line('self代表类的实例，而非类')
em = Employee('pony', 10000)
em.prt()
print_split_line('创建 Employee 类的第一个对象，调用方法，访问属性')
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
# print("Total Employee: %d" % Employee.empCount)
emp1.displayCount()

print_split_line('添加，删除，修改类的属性')
emp1.age=12
print(emp1.age)
emp1.age=15
print(emp1.age)
del emp1.age

print_split_line('也可以使用以下函数的方式来访问属性：')
'''
    getattr(obj, name[, default]) : 访问对象的属性。
    hasattr(obj,name) : 检查是否存在一个属性。
    setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
    delattr(obj, name) : 删除属性。
'''
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
print(hasattr(emp1, 'age'))    # 如果存在 'age' 属性返回 True。
print(getattr(emp1, 'age') )   # 返回 'age' 属性的值
delattr(emp1, 'age')    # 删除属性 'age'
print(hasattr(emp1,'age'))

print_split_line('Python内置类属性')
'''

    __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
    __doc__ :类的文档字符串
    __name__: 类名
    __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
    __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

'''
print("Employee.__doc__:", Employee.__doc__       )
print("Employee.__name__:", Employee.__name__     )
print("Employee.__module__:", Employee.__module__ )
print("Employee.__bases__:", Employee.__bases__   )
print("Employee.__dict__:", Employee.__dict__     )