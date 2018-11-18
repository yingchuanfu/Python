# -*- coding: UTF-8 -*-

#定义一个简单的类,描述一个人的基本信息
class Person:
    #定义类的数据成员:姓名,年龄
    name = ''
    age = 0

    #定义一个函数:打印类实例的基本信息
    def printPersionInfo(self):
        print('persion-info:{name:%s, age:%d}'%(self.name, self.age))
    #定义一个简单的函数
    def hello(self):
        print("hello world!")

#实例化,创建一个对象
p = Person()
#访问类的属性:数据成员,访问语法obj.x
print("name:", p.name)
print("age:", p.age)
#访问类的函数
p.printPersionInfo()
p.hello()

#self参数
class Person:
    #定义类的数据成员:姓名,年龄
    name = ''
    age = 0

    #定义一个函数:打印类实例的基本信息
    def printPersionInfo(self):
        print('name:', self.name)
        print('self:', self)
        print('self class:', self.__class__)


#实例化,创建一个对象
p = Person()
#访问类的函数
p.printPersionInfo()
