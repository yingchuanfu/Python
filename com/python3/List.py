# -*- coding: UTF-8 -*-
#数据结构:列表(list)

#创建列表:用方括号 [] 定义
list1 = [3.14, 5.96, 1995, 2018, "china", 3+4j] #同一个列表中可以存放任意基本数据类型(包含浮点型 整形 字符串和复数)
list2 = [1, 2, 3, 4, 5]
list3 = ["BeiJing", "ShangHai", "GuangZhou", "ShenZhen"]
list4 = [] #创建一个空列表

#访问列表中的元素(通过索引下标访问列表中的元素,可以一次访问一个或多个元素)
#通过索引下标访问列表中的单个元素
print("list1[2]:", list1[2])
print("list1[2]:", list2[2])
print("list1[2]:", list3[2])
#通过索引下标一次访问多个元素
print("list1[2]:", list1[0:2])

#更改列表中的元素
list1 = [3.14, 5.96, 1995, 2018, "china", 3+4j]
print("before list[3]:", list1[3])
list1[3] = "Change"
print("after list[3]:", list1[3])
print("==========================================")

#删除列表中的元素:Python提供三种删除列表中元素的方法del remove(obj) clear()
#删除列表中的元素
list1 = [3.14, 5.96, 1995, 2018, "china", 3+4j]
print("before the operation:", list1)
del list1[3]
list1.remove(3+4j)
print("after deleting the element:", list1)
#清空列表元素
list1.clear()
print("after the emptying of the list:", list1)

#向列表中添加新元素
list1 = [3.14, 5.96, 1995, 2018, "china", 3+4j]
#append(object):添加新元素到列表末尾
list1.append("New Element-I")
#insert(index,object):插入新元素到指定索引位置
list1.insert(2, "New Element-II")
print("after add new element list1:", list1)


print("列表常用内建方法============================")
list1 = [2013, 1995, 2016, 2017, 2020, 1949]
#求列表长度,即列表中元素的个数:len(obj)
print("the length of the list:", len(list1))
#求列表中元素的最大值:max(list)
print("the largest element in the list:", max(list1))
#求列表中元素的最小值:min(list)
print("the smallest element in the list:", min(list1))
#统计某个元素在列表中出现的次数: list.count(obj)
print("the number of times 1949  appears:",list1.count(1949))
#从列表中找出某个值第一个匹配项的索引位置:list.index(obj)
print("the index of the first location of 1949:", list1.index(1949))
#复制一个已有的列表:list.copy()
copyList1 = list1.copy()
print("copyList1:", copyList1)
#反转一个已有的列表:list.reverse()
list1.reverse()
print("after reversing:", list1)

#列表常用操作:列表拼接 列表乘法 迭代 嵌套等
print("===================================")
list1 = [1, 2, 3, 4]
list2 = [5, 6, "BeiJin", 7, 8]
#列表拼接
print("list1 + list2:", list1+list2)
#列表乘法
print("list1*2", list1*2)
#判断元素是否存在于列表中
print("3 in list1?", 3 in list1)
print("300 in list1?", 100 in list1)
#迭代
for element in list1:print(element)
#列表嵌套
list3 = [list1, list2]
print("list3:", list3)