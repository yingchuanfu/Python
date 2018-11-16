# -*- coding: UTF-8 -*-
#数字和运算符

#数字
#phthon提供了三种数字类型,即int(整形), float(浮点型), complex(复数)
# int：通常被称为整型或者整数，如100、99、1、3都属于整型；
# float：浮点数包含整数和小数部分，如3.1415，12.578712；
# complex：复数包含实数部分和虚数部分，形如 a+bj，其实部和虚部都是浮点类型。
# 需要注意的是，Python3 已经废弃了 Python2 的 Long（长整型），在 Python3 中，int 的大小没有限制，可以作为 Long 使用

#数字类型转换
#python的三种数字类型可以进行转换,转换方式为:数字类型+圆括号

a = 123
b = 3.1415926
print("int(b)=",int(b))
print("float(a)=",float(a))
print("complex(a)=",complex(a))
print("complex(a,b)=",complex(a,b))

print("常用的数学函数================================================")
#常用的数学函数
import math
#求绝对值abs(x)
print("abs(-5)=",abs(-5))

#向上取整ceil(x)
print("ceil(3.14)=",math.ceil(3.14))

#向下取整floor(x)
print("floor(3.678)=",math.floor(3.678))

#四舍五入round(x)
print("round(3.678)=",round(3.678))

#乘方运算pow(x,y),x的y次方
print("pow(3,4)=",pow(5,3))

#求平方根sqrt(x)
print("sqrt(121)=",math.sqrt(121))
