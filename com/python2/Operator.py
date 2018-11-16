# -*- coding: UTF-8 -*-
#数字和运算符
print("常用的运算符大致7种================================")
#python常用的运算符大致7种,分为算术运算符, 比较运算符, 赋值运算符, 逻辑运算符, 位运算符, 成员运算符, 身份运算符
print("一:算术运算符7")
#python中的算术运算符有7种:加(+) 减(-) 乘（*）除(/) 取模(%) 幂运算(**)和取整运算(//)
#初始化数据
x = 24
y = 5
z = 0

z = x + y
print("x+y=", z)
z = x - y
print("x-y=", z)
z = x * y
print("x*y=", z)
z = x / y
print("x/y=", z)
z = x % y
print("x%y=", z)
z = x ** y
print("x**y=", z)
z = x // y
print("x//y=",z)

print("二: 比较运算符6=====================")
#python提供了6种比较运算符:大于(>) 小于(<) 等于(==) 不等于(!=) 大于或等于(>=) 小与或等于(<=);比较运算符的结果是一个布尔值,true或者false
#初始化数据
x = 24
y = 5
print("x>y:", x > y)
print("x<y:", x < y)
print("x==y:", x == y)
print("x>=y:", x >= y)
print("x<=y:", x <= y)
print("x != y:", x != y)

print("三:赋值运算符7======================")
#如x = 25就是一个简单的运算, "="就是最简单的赋值运算符;将简单的赋值运算符与算术运算符结合,python形成了丰富的赋值运算符:+= -= = /= %= *= //=
#初始化数据
x = 2
y = 3
y = x
print("y=x, y=", y)
y += x
print("y+=x, y=", y)
y -= x
print("y-=x, y=", y)
y *= x
print("y*=x, y=", y)
y /= x
print("y/=x, y=", y)
y **= x
print("y**=x, y=", y)
y //= x
print("y//=x, y=", y)

print("四:逻辑运算符3=========================")
#python种逻辑运算符分别为:and(与) or(或）not(非),逻辑运算符的结果是布尔值：true或者false
#1 A and B:当A为false时, 运算结果为false;否则返回B的值
#2 A or B:当A为true时, 运算结果为A的值;否则返回B的值
#3 notA:当A为true时,返回false,否则返回true
x = 2
y = 3
z =  5
print("x>y and x<z:", x > y and x < z)
print("x<y and z:", x < y and z)

print("x>y or z:", x > y or z)
print("x<y or z:", x < y or z)

print("not x:", not x)
print("not x < y:", not x < y)

print("五:位运算符===============================")
print("六:成员运算符=============================")
#成员运算符的结果为布尔值True或者False
#初始化一个字符串和列表
temp1 = "ABCDEFG"
temp2 = [4, 2, 3, 5, 8, 9]
a = "CDE"
b = 5
c = "CDF"
print("a in temp1?", a in temp1)
print("b in temp2?", b in temp2)
print("c in temp1?", c in temp1)
print("七:身份运算符=============================")