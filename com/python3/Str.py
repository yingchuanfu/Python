# -*- coding: UTF-8 -*-
#数据结构，包括字符串、列表、元组、字典、栈、队列和集合

#一:创建字符串,并为变量赋值
str1 = "Hello World!"
str2 = "yingchuanfu"

#二:访问字符串中的元素(一个字符串可以看成若干个字符元素组成,python中可以通过索引来访问字符串中的元素,也可以访问子串)
str1 = "Hello world!"
#访问字符串中的单个字符或者子串
print('str1:', str1)
print('str1[0]:', str1[0])
print('str1[0:5]:', str1[0:5])
print('str1[5:9]:', str1[6:11])

#三:修改字符串(python字符串修改需要通过内建replace(old,new)方法,不支持直接通过索引对已有内容的修改,此外还支持对字符串拼接)
str1 = "Hi!"
str2 = "python"
#通过拼接修改字符串
str1 = str1 + str2
print("after splicing str1:",str1)
#通过替换修改字符串:replace(old,new)
str1  = str1.replace(str2, "yingchuanfu")
print('after replacement str1:',str1)

#四:字符串运算符(字符串是一种灵活的数据结构,可以进行拼接 剪切 复制等操作)
str1 = 'hello world!'
str2 = 'python'
#字符串拼接
print('str1+str2:', str1+str2)
#字符串截取
print('str1[0:6]:', str1[0:6])
#字符串复制
print('str2*2:', str2*3)
#成员运算,判断一个字符串是否包含某成员
print('world in str1?', 'world' in str1)
print('world in str1?', 'word' in str1)

#五:字符串格式化
#格式化为十进制:%d
print('pi is approximately equal to %d (I)'%(3.1415926))
#格式化字符串
print('pi is approximately to equal to %s (II)'%3.1415926)
#格式化浮点数字,指定小数点后的精度,默认为6位小数:%f
print('pi is approximately equal to %f (III)'%(3.1415926))
#格式化浮点数字,指定n位小数:.nf
print('pi is approximately to euqual to %.2f (IV)'%(3.1415926))
#用科学计数法格式化浮点数:%e
print('pi is approximately equal to %e (V)'%(3.1415926))

#格式化为十进制:%d
print('The road is about %d meters long (VI)'%(1234))
#格式化无符号八进制数:%o(不是数字0,小写字母o)
print('The road is about %o meters long (VII)'%(1234))
#格式化无符号十六进制数:%x
print('The road is about %x meters long (VIII)'%(1234))

#六:字符串内建函数(python为字符串提供了40余个内建函数，在此介绍常用的)
print('字符串常用内建函数========================')
str1 = "  Hello world! Hello"
str2 = "Hello"

#返回字符串的长度:len(str)
print('str1的长度:', len(str1))
#对字符串进行分割:split(str),分割符为str,此处以空格进行分割
print('str1以空格分割的结果：', str1.split(' '))
#删除字符串首尾的空格
print('str1删除首尾空格:', str1.strip())
#count(str2, beg>=0,end<=len(str1)
#返回str2在str1里面出现的次数,如果beg或者end指定则返回指定范围内str2出现的次数
print('str2在str1出现的次数:', str1.count(str2))
print('str2在str1中出现的次数(指定范围):', str1.count(str2, 10, 20))

#检查字符串是否以 obj 结束, 如果beg 或者 end 指定则检查指定的范围内是否以 obj结束
#如果是, 则返回True, 否则返回False
print('str1是否以 str2结尾:', str1.endswith(str2))
print('str1是否以 str2结尾(指定范围):', str1.endswith(str2, 10, 19))

#检测str2是否包含在字符串str1中, 如果指定范围beg 和end ,则检查是否包含在指定范围内
#如果包含返回开始的索引值,否则返回-1
print('str1中是否包含str2:', str1.find(str2))
print('str1中是否包含str2(指定范围):', str1.find(str2, 10, 20))