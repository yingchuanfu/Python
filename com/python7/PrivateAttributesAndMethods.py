# -*- coding: UTF-8 -*-
print("私有属性与私有方法================")
#1定义私有属性:__attribute:属性名前加两个下划线,即声明该属性为私有,不能在类的外部直接访问,在类的内部访问时用self.__attribute
#2定义私有函数:__funtion:函数名前面加两个下划线,即声明该函数为私有,不能再类的外部直接访问,在类的内部访问时用self.__function

#定义一个简单的类,描述一个人的基本信息
class Person:
    #定义两个私有属性:name, age
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    #定义公有函数,在类外部可以访问
    def getName(self):
        self.__fun()
        return self.__name
    def getAge(self):
        return self.__age

    #定义一个私有函数,只能在类内部使用
    def __fun(self):
        print('hello world!')

#实例化
p1 = Person("ZhangSan", 12)
#访问类的私有属性和私有函数,将会报错
# print("name:", p1.__name)
# print("age:", p1.__age)
# p1.__fun()



#对于私有属性和私有函数,如果需要在类外部访问,可以通过公有函数实现(与java和c++一致)
#访问类的公有函数
print("name:", p1.getName())