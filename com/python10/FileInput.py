# -*- coding: UTF-8 -*-
#一:使用fileinput进行迭代

import fileinput
for line in fileinput.input("F:/python2.txt"):
    print(line)
    print("当前文件的名称:",fileinput.filename())
#input函数有多个参数:分别设置读取文件路径 读写模式 编码方式 缓冲区大小 备份文件拓展名等
#fileinput模块有很多常用的函数,介绍几个常用的,可根据模块分析方法自行挖掘

#dir()函数,模块分析
print("模块分析===============================")
import fileinput
print(dir(fileinput))

#fileinput.input():返回能够用于for循环遍历的对象
#fileinput.filename():返回当前文件的名称
#fileinput.lineno():返回当前已经读取的行的数量(或者序列)
#fileinput.filelineno():返回当前读取的行的行号
#fileinput.isfirstline():检查当前行是否是文件的第一行
#fileinput.isstdin():判断最后一行是否从stdin中读取
#fileinput.close():关闭队列


#二:文件迭代器(Python从2.2开始,文件对象具备可迭代性)
print("文件迭代器=================================")
f = open("F:/python2.txt", 'w') #打开文件,一次写入多行内容
content = ['append python3.7.1\n', 'append 2018']
f.writelines(content)
f.close()
#打开文件,通过文件迭代器遍历文件
f = open("F:/python2.txt", 'r')
for line in f:
    print("content:", line)
#关闭文件
f.close()

#借助文件迭代器,可以执行和普通迭代器相同的操作
print("将读取内容转化为字符串列表（效果类似前面介绍的readlines)")
f = open("F:/python2.txt", 'w')
content = ['append Java vs Python\n', 'Python NO1']
f.writelines(content)
f.close()

f = open("F:/python2.txt", 'r')
lines = list(f)
print(lines)
f.close()