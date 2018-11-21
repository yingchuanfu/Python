# -*- coding: UTF-8 -*-

#多继承实例
#定义一个类BankAccount,描述银行账户
class BankAccount:
    def __init__(self, number, balance):
        self.nuber = number
        self.balance = balance

    #计算并返回年利息
    def getAnnualInterest(self):
     return self.balance*0.042

    def printInfo(self):
        print('BankAccount-info')

#定义一个类Occupation,描述职业
class Occupation:
    def __init__(self, salary, industry):
        self.salary = salary
        self.industry = industry
    def printOccupationInfo(self):
        print('Occupation-info:{salary:%d, industry:%s}'%(self.salary,self.industry))

    def printInfo(self):
        print('Occupation-info')

#定义一个类Person,继承自类BankAccount和Occupation
class Person(Occupation,BankAccount):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #定义一个函数:打印类实例的基本信息
    def printPersonInfo(self):
        print('person-info:{name:%s, age:%d'%(self.name,self.age))

    # def printInfo(self):
    #     print('person-info')
#创建一个子类对象
temp = Person('Wu-Jing', 38)
#访问父类数据成员
temp.nuber = 622202050201
temp.balance = 1000000.99
temp.salary = 21000
temp.industry = "IT"

#分别调用本身和父类的函数
temp.printOccupationInfo()
temp.printPersonInfo()
print('Annual interest:', temp.getAnnualInterest())


print("子类使用父类同名的函数或属性,在没有指定的情况下,Python多继承根据顺序从左到右查找")
temp.printInfo()