#! /usr/bin/python
# -*- coding: UTF-8 -*-

class Father(object):
    def __init__(self, name):
        self.name = name
        print("Father name: %s" % (self.name))

    def getName(self):
        return 'Father ' + self.name

class Mother(object):
    def __init__(self, name):
        self.name = name
        print("Mother name: %s" % (self.name))

    def getName(self):
        return 'Mother ' + self.name

class Son(Father, Mother):
    def __init__(self, name):
        super(Son, self).__init__(name)
        Father.__init__(self, name) #super 继承父类的构造方法时，只继承以第一个父类方法
        Mother.__init__(self, name)
        print("hi")
        self.name = name

    def getName(self):
        return 'Son ' + self.name

if __name__ == '__main__':
    s = Son('pony')
    print(s.getName())
