# -*- coding: UTF-8 -*-
print("hello world");

#python中变量没有类型与java.c++不同
a = 2;
print("a=", a);
a = "yingchuanfu";
print("a=", a);
a = 5+4j;
print("a=", a);

#自定义函数,求两个数的和
def add(a, b):
    return a + b

#直接调用内建函数pow(x,y),计算x的y次方
print('5的三次方 = %d' %pow(5,3))
print('1+2 = %d' %add(1,2))