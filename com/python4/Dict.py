# -*- coding: UTF-8 -*-
#数据结构，包括字符串、列表、元组、字典、栈、队列和集合

#字典(dictionary):可以理解为一种映射表,存储Key-value(键值对)类型数据的容器
#字典的三点注意事项:1同一个字典中,键必须是唯一的,不存在两个相同的键,键的值不能改变,数据类型可以是数字,字符串或者元组;
#2同一个字典中,值不必唯一,值可以是任意数据类型;
#3字典定义采用花括号 {},键值之间用冒号隔开,键值对之间用逗号隔开;

#创建字典
dictName = {"id01":"zhangsan", "id05":"lishi", "id10":"wangwu"}
dictAddress = {1:"beijin", 3:"shanghai", 5:"shenzhen"}
dict3 = {"excellent":100, "good":80, "pass":60, "fail":50}
#字典也可以嵌套
dict4 = {"A": ["liTong","liMing"], "B":["xiaoHong","xiaoHua"]}

#访问字典中的元素:1直接通过键来访问;2通过内建get(key)方法访问
print("dict3['good']:", dict3['good'])
print("dictAddress[1]:", dictAddress[1])
print("dict3.get('good'):", dict3.get('good'))

#修改字典中的元素
dict3['good'] = 85
print("dict3['good']:", dict3.get('good'))

#删除字典中的元素或字典
#删除字典中的一个元素
del dict3['good']
print("dict3:", dict3)
#删除字典:del dict3

#使用内建方法pop(key)删除指定元素
dict3.pop('pass')
print("dict3:",dict3)
#清空字典
dict3.clear()
print("dict3:",dict3)

#字典的常用内建方法
dict5 = {"excellent":100, "good":80, "pass":60, "fail":50}
#计算字典的长度
print("the length of the dict5:", len(dict5))
#获取字典中所有的键
print("get all the keys in dict5:\n", dict5.keys())
#获取字典中所有的值
print("get all the values in dict5:\n", dict5.values())
#获取字典中所有的键值对
print("get all the key-value pairs in dict5:\n", dict5.items())