# -*- coding: UTF-8 -*-
#抽象函数:类(在Python中,类具有封装,继承,多态,但是没有重载)

#self参数
class Person:
    #定义类的数据成员:姓名,年龄
    name = ''
    age = 0
    #定义构造函数,用于创建一个类实例,也就是类的具体对象
    #通过参数传递,可以赋予对象初始状态
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #定义一个函数:打印类实例的基本信息
    def printPersionInfo(self):
        print('person-info:{name:%s, age:%d}'%(self.name, self.age))

#实例化,创建二个对象,默认调用构造函数: _init_
p1 = Person("ZhangSan", 12)
p2 = Person("Li Si", 18)
#访问类的属性: 数据成员,访问语法obj.x
print("name:", p1.name)
print("age:", p1.age)
#调用类的函数
p1.printPersionInfo()
p2.printPersionInfo()
