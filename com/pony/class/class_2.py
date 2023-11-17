#! /usr/bin/python
# -*- coding: UTF-8 -*-

'''
python对象销毁(垃圾回收)
Python 使用了引用计数这一简单技术来跟踪和回收垃圾。

垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。
这种情况下，仅使用引用计数是不够的。Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。作为引用计数的补充，
 垃圾收集器也会留心被分配的总量很大（即未通过引用计数销毁的那些）的对象。 在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。
'''
from __future__ import print_function
from __init__ import print_split_line

print_split_line('析构函数,對象回收')


# __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):  # 析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
        class_name = self.__class__.__name__
        print(class_name, "销毁")


p1 = Point()
p2 = p1
p3 = p2
print(id(p1), id(p2), id(p3))
del p1
del p2
del p3

print_split_line('类的继承')


class Parent:
    parentAttr = 100

    def __init__(self):
        print('调用父类构造函数')

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent, Point):

    def __init__(self):
        print('调用子类构造方法')

    def childMethod(self):
        print('调用子类方法')


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值
print('布尔函数判断一个类是另一个类的子类或者子孙类:', issubclass(Child, Parent))
print('布尔函数判断一个类是另一个类的子类或者子孙类:', issubclass(Child, Point))
print('布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象:', isinstance(c, Child))
print('布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象:', isinstance(c, Parent))
del c

print_split_line('方法重写')


class Child_2(Parent):
    def parentMethod(self):  # 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：
        print('调用子类方法')


c2 = Child_2()
c2.parentMethod()

print_split_line('基础重载方法')
'''
1	__init__ ( self [,args...] )
构造函数
简单的调用方法: obj = className(args)
2	__del__( self )
析构方法, 删除一个对象
简单的调用方法 : del obj
3	__repr__( self )
转化为供解释器读取的形式
简单的调用方法 : repr(obj)
4	__str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
5	__cmp__ ( self, x )
对象比较
简单的调用方法 : cmp(obj, x)
'''


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('调用构造方法: ', self)

    def __del__(self):  # 在程序执行文成，自动调用
        print('调用析构方法，回收对象: ', self)

    # def __repr__(self):
    #     print('调用__repr__方法')
    #     return self.__str__()

    def __str__(self):
        # print('调用__str__方法')
        return 'A (%d, %d)' % (self.a, self.b)

    def __cmp__(self, other):
        # print('调用__cmp__ 方法')
        return self.a + self.b > other.a + other.b

    def __add__(self, other):
        return A(self.a + other.a, self.b + other.b)


a1 = A(1, 3)
a2 = A(1, 2)
print(repr(a1))
# print(str(a))
print(a1.__cmp__(a2))
print(a1 + a2)
del a1
del a2

print_split_line('类属性与方法')
'''
类的私有属性

__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
类的方法

在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
类的私有方法

__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods 
'''


class JustCounter:
    public_var = 0
    _protected_var = 0
    __private_var = 0

    def __init__(self,public_var_1,_protected_var_1,__private_var_1):
        self.public_var_1 = public_var_1
        self._protected_var_1 = _protected_var_1
        self.__private_var_1 = __private_var_1

    def count(self):
        self.__private_var += 1
        self.public_var += 1

    def getPrivateVar(self):
        return self.__private_var

    def getProtectedVar(self):
        return self._protected_var

    def getPublicVar1(self):
        return self.public_var_1

    def getPrivateVar1(self):
        return self.__private_var_1

    def getProtectedVar1(self):
        return self._protected_var_1

class ChildJustCounter(JustCounter):
    _protected_var = 12



jc1 = JustCounter(11,22,33)
jc1.count()
jc1.count()
print(jc1.public_var)
print(jc1.getPrivateVar())
print(jc1._JustCounter__private_var)  # Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性
print(jc1.public_var_1)

jc2 = ChildJustCounter(111,222,333)
print(jc2.getProtectedVar())
print(jc2.getPublicVar1())
print(jc2.getProtectedVar1())
# print(jc2.getPrivateVar1()) #AttributeError: 'ChildJustCounter' object has no attribute '_ChildJustCounter__private_var_1'
print(jc1.getPrivateVar1()) #父类私有的方法，子类不能访问（不能取值/不能赋值）


