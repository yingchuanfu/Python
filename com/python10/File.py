# -*- coding: UTF-8 -*-
#open(file, model, buffering)用于打开文件并返回一个文件对象,open函数的参数中,
#文件名file是强制参数,模式(model)和缓冲(buffering)都是可选的

print("一:打开文件")
#打开文件读取其中全部内容
f = open("F:/python.txt")
print(f.read())

print("二:文件模式")
#二.文件模式参数:r,读模式; a,追加模式; b二进制模式; +,读写模式;w,写入模式
#例1.打开文件,写入文本
f = open("F:/python.txt", 'w')
f.write("learn python")
# 打开文件,读取文本
f = open("F:/python.txt", 'r')
print(f.read())
#关闭文件
f.close()

#例2
#打开文件,在现有文件后追加信息并换行
f = open("F:/python.txt", 'a')
f.write('\n append information')
f.close()
#打开文件,读取文本
f = open("F:/python.txt", 'r')
print(f.read())
#关闭文件
f.close()

print("三:缓冲")
print("四:读写文件")
#open函数返回的只是一个文件对象,读写文件需要调用read函数和write函数,完成读写后,需要调用close函数
#read函数可以带参数,指定读取的字节数,不带参数则默认读取文件全部内容.write函数参数为字符串类型,即写入文件的内容

#打开文件,在现有文件后追加信息并换行
f = open("F:/python.txt", 'a')
f.write('\n append cotent')
f.close()

#打开文件,读取文件前4个字节
f = open("F:/python.txt", 'r')
print(f.read(4))
#关闭文件
f.close()

print("五:读写行")

#例子1:不带参数
print("1不带参数================")
#打开文件,写入信息并换行
f = open("F:/python2.txt", 'w')
f.write('append information\n')
f.write('append information2\n')
f.write('append information3\n')
f.close()

#通过readline()函数遍历文件
#打开文件,按行读取文件内容
f = open("F:/python2.txt", "r")
while True:
    line = f.readline()
    #读取完毕退出
    if (not line):
        break
    print('content:', line)
#关闭文件
f.close()


#例子2:带参数
print("2带参数==================")
f = open("F:/python2.txt", 'w')
f.write('append information4\n')
f.close()
f = open("F:/python2.txt", 'r')
while True:
    line = f.readline(10)
    if (not line):
        break
    print('content:', line)
f.close()

#readline函数每次读取一行,与之对应的readlines则可一次读取整个文件的所有行
f = open("F:/python2.txt", 'w')
f.write('append information5\n')
f.write('append information6')
f.close()
f = open("F:/python2.txt", 'r')
for line in f.readlines():
    print('content:', line)
#关闭文件
f.close()

print("通过writelines函数,可以一次向文件写入多行内容")
f = open("F:/python2.txt", 'w')
content = ['append information7\n', 'append information8']
f.writelines(content)
f.close()
f = open("F:/python2.txt", 'r')
for line in f.readlines():
    print('content:', line)
f.close()