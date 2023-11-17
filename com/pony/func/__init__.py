# encoding: utf-8

# functions

def printme(str):
    # 打印传入的字符串到标准显示设备上
    print('=================' + str + '=================')
    return


printme('aaaaaaa')

'''
参数传递
可更改(mutable)与不可更改(immutable)对象

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

    不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

    不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

    可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''

printme('传不可变对象实例')


def ChangeInt(a):
    a = 10
    pass


b = 2

ChangeInt(b)
print(b)

printme('传可变对象实例')


def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    mylist[0] = 9
    print("函数内取值: ", mylist)
    return


mylist = [1, 2, 3]
changeme(mylist)
print("函数外取值: ", mylist)

'''
参数类型：

    必备参数
    关键字参数
    默认参数
    不定长参数

'''
printme('必备参数')


def f0(str):
    "打印任何传入的字符串"
    print(str)
    return


f0('as')  # 必须传入参数

printme('关键字参数')


# 可写函数说明
def f1(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用printme函数
f1(str="My string")
f1("My string")


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="miki")
printinfo(50, "miki")

printme('默认参数')


# 可写函数说明
def f2(name='pony'):
    "打印任何传入的字符串"
    print("Name: ", name)
    return


# 调用printinfo函数
f2()
f2('lisi')

printme('不定长参数')


# 可写函数说明
def f3(*vartuple):
    "打印任何传入的参数"
    print("输出: ")
    for _var in vartuple:
        print(_var)
    return


# 调用printinfo 函数
f3(12)
f3()
f3(1, 2, 3, 4)

printme('匿名函数')
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))

printme('return 语句')
# 可写函数说明
def f4( arg1, arg2 ):
    # 返回2个参数的和."
    total = arg1 + arg2
    return total

# 调用sum函数
total = f4(10, 20)
print(total)

printme('变量作用域')
total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total

#调用sum函数
sum( 10, 20 )
print("函数外是全局变量 : ", total)