# -*- coding: UTF-8 -*-
print("函数重写Override===========")
#定义一个类Occupation,描述职业
class Occupation:
    #定义构造函数
    def __init__(self, salary, industry):
        self.salary = salary
        self.industry = industry
    def printInfo(self):
        print('salary:%d, industry:%s'%(self.salary, self.industry))

#定义一个简单的类Person,继承自类Occupation
class Person(Occupation):
    def __init__(self, name, age):
        self.name  = name
        self.age  = age
    #定义一个函数:打印类实例的基本信息
    def printInfo(self):
        print('name:%s,age:%d'%(self.name,self.age))
        print('salary:%d,industry:%s'%(self.salary,self.industry))

#创建一个子类对象
temp = Person('Wu-Jing', 38)
#访问父类的数据成员
temp.salary = 21000
temp.industry = "IT"
#分别调用函数printInfo()
temp.printInfo()