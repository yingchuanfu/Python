# -*- coding: UTF-8 -*-
#数据结构，包括字符串、列表、元组、字典、栈、队列和集合

#集和:集合(set)是一个数学概念,是由一个或多个确定的元素所构成的整体
#结合具有的三个特点:1确定性,集合中的元素必须是确定的; 2互异性,集合中的元素互不相同; 3无序性,集合中的元素没有先后之分

#创建集合:用大括号({}),如果要创建一个空集合,必须用set()而不是{};后者创建一个空的字典
country1 = {'china', 'america', 'german'}
country2 = set('china')
country3 = set()
print("country1:", country1)
print("country2:", country2)
print("country3:", country3)
print("============================")

#操作集合中的元素(可以访问集合中的元素,也可增加,移除元素)
setA = {'a', 'b', 'c'}
print("setA", setA)
setA.add('d')
print("setA.add('d'):", setA)
setA.add('a')
print("setA.add('a')互异性元素互不相同:", setA)
setA.remove('a')
print("setA.remove('a'):", setA)
print("=============================")

#集合运算:对于集合可以计算交集 并集 补集
setA = {'A','B','C'}
setB = {'D','C','E'}
#交集
print("setA & setB:", setA & setB)
#并集
print("setA | setB:", setA | setB)
#差集
print("setA -  setB:", setA - setB)