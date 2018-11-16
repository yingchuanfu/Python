# -*- coding: UTF-8 -*-
#数据结构:栈(stack)
#定义:通过append(obj)函数最后添加的元素,可以通过pop()函数最先取出来,也就是"后进先出",这种数据结构称为"栈"

#初始化一个列表
stack = [1, 2, 3, 4, 5]
#append(obj):添加元素到列表尾部
stack.append(666)
print("stack:", stack)
#pop():从列表尾部取出元素
print("stack.pop():", stack.pop())