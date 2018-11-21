# -*- coding: UTF-8 -*-
print("一:函数的定义与调用=====================")
#Python中函数的定义:无需声明返回值类型,也无需修饰符
#定义形式:函数定义符,函数名(参数列表)
#def getPath(basePath, fileName):
#def getName();

#定义函数
def compare(parameter1, parameter2):
    if (parameter1 > parameter2):
        print(1)
    elif (parameter1 == parameter2):
        print(0)
    else:
        print(-1)

#函数调用
compare(123, 456)
compare(5, 1)
compare(5,5)

print("二:参数传递=====================")
#变量与引用(在Python中,所有类型:函数 模块 数字 字符串 列表 元组 字典等等都是对象,而变量是没有类型的)
#实例
a = 12
print("a=", a)
a = "ABCDE"
print("a=", a)
a = [1, 2, 3, 4, 5]
print("a=", a)
a = (1, 2, 3, 4, 5)
print("a=", a)
a = {'key': 12, 'key2': 13}
print("a=", a)

#不可变类型(只能通过创建新的对象才能改变对变量的赋值的数据类型,称为不可变类型,如整数 字符串 元组都是不可变类型)
def change(x):
    x = 10
a = 5
change(a)
print("a=", a)

#可变类型(包括列表 字典 集合 队列等)
def change(x):
   x.append(2018)

a = [2015, 2016, 2017]
change(a)
print("a=", a)


print("三:函数的参数类型==============================")
#Python中,函数的参数有四种类型:必须参数 关键字参数 默认参数和不定长参数)
print("1必须参数")

#实例1):参数数量要对应
#声明参数为一个
def update(arg):
    arg = arg + 1
#正确
update(12)
#不正确,参数缺失
#update()
#不正确,参数多余
#update(1, 2)

#实例2)参数顺序要一致
def printInfo(name, sex, age):
    print("name:", name)
    print("sex:", sex)
    print("age:", age)
#正确
printInfo("Jack", "male", 18)
#错误,参数顺序不对应
#printInfo(18, "Jack", "male")



print("2关键字参数")
def printInfo(name, sex, age):
    print("name:", name)
    print("sex:", sex)
    print("age:", age)
#都是正确的
printInfo(name="tomYing", sex="femal", age=18)
printInfo(sex="femal", name="tomYing", age=18)
printInfo(sex="femal", age=18, name="tomYing")



print("3默认参数")
def printInfo(name, sex, age=0):
    print("name:", name)
    print("sex:", sex)
    print("age:", age)
#正确
printInfo(name="yingchuanfu", sex="male")



print("4不定长函数")
#定义一个求和函数
def sum(num, *num_list):
    sum = num
    for element in num_list:
        sum += element
    print("sum=", sum)

sum(1)
sum(1, 2, 3, 4)


print("四:return语句========================")
#定义比较函数
def compare(parameter1, parameter2):
    if (parameter1 > parameter2):
        return 1
    elif (parameter1 == parameter2):
        return 0
    else:
        return -1

result = compare(123, 456)
print("result=", result)


print("五:变量作用域========================")
#这里的a是全局变量
a = 123
def function():
    a = 10 #这里的a是局部变量
    print("I a=", a)
function()
print("II a=", a)
#作用域分类:按作用域不同,变量可分为四种类型:
# L(Local),局部作用域;
# E(Enclosing),闭包函数外的函数中;
# G(Global),全局作用域;
# B(Built-in),内建作用域;
#使用变量时,会根据作用域进行查找,优先级顺序为:L->E->G->B
