# -*- coding: UTF-8 -*-
#数据结构，包括字符串、列表、元组、字典、栈、队列和集合

#元组与列表的区别:1定义方式不一样: 列表采用方括号 [], 元组采用圆括号 ();
#                 2元组中的元素不能改变,元组一旦创建就不能再对其中的元素进行增 删 改,只能访问

#创建元组
tuple1 = () #同一个元组中可以没有数据
tuple2 = (12,) #如果元组只有一个元素,那么这个元素后面要加逗号,否则将被认为是一个基本数据类型,而不是元组
tuple3 = (1, 2, 3, 4, 5)
tuple4 = (3.14, 5.96, 1995, 2020, "china", 3+4j) #同一个元组中可以存放任意数据类型
tuple5 = 4, 5, 6, 7 #创建元组可以没有括号,元素之间用逗号分隔开即可

#访问元组中的元素
tuple = (3.14, 5.96, 1995, 2020, "china", 3+4j)
print("tuple[2]:", tuple[2])
print("tuple[1:3]:", tuple[1:3])

#元组相关的常用内建方法
tuple6 = (3.14, 5.96, 1995, 2020, 1949)
#求元组长度,即元组的个数:len(tuple)
print("the length of the tuple:", len(tuple6))
#求元组中元素的最大值:max(tuple)
print("the largest element in the tuple:", max(tuple6))
#求元组中元素的最小值:min(tuple)
print("the smallest element in the tuple:", min(tuple6))
#统计某个元素在元组中出现的次数:tuple.count(obj)
print("the number of times 1949 appears:", tuple6.count(1949))
#从元组中找出某个值第一个匹配项的索引位置:tuple.index(obj)
print("the index of the first location of 1949:", tuple6.index(1949))

#元组常用的操作(元组常用的运算操作与列表相同:包括元组拼接 元组乘法 迭代 嵌套等)
tuple7 = (1, 2, 3, 4)
tuple8 = (5, 6, "BeiJin", 7, 8)
#元组拼接
print("tuple7 + tuple8:", tuple7 + tuple8)
#元组乘法
print("tuple7*2:", tuple7 * 2)
#判断元素是否存在于元组中
print("3 in tuple7?", 3 in tuple7)
print("3 in tuple8:", 3 in tuple8)
#迭代
for element in tuple7:print(element)
#元组嵌套
tuple9 = [tuple7, tuple8]
print("tuple9:", tuple9)