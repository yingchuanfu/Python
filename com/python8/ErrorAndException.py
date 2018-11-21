# -*- coding: UTF-8 -*-
#在Python中,可以将出错归为两类:错误(Errors)和异常(Exception)

#一.错误:从软件方面来说,一般将错误分为两种:语法错误,逻辑错误
print("语法错误==================")
#少了一个冒号:
#while True
#    print("hello world")
print("逻辑错误===================")
#比较两个数,返回较大值,漏掉了相等的情况
def compare(num1, num2):
    if (num1 > num2):
        return num1
    elif (num1 < num2):
        return num2
print("result:", compare(5, 5))


#二.异常
num_list = [12, 34, 56, 78, 90]
#下标索引超出序列边界
#print(num_list[14])

print("异常的处理====================")
def compare(num1, num2):
    try:
        if (num1 >= num2):
             return num1
        else:
             return num2
    except:
        return "ERROR"

#正确的调用
print("compare(12,5):", compare(12, 5))
#异常调用
print("compare(12,'ad'):", compare(12, 'ab'))
print("compare(12,15):", compare(12, 15))

print("try与else语句结合使用=============")
#如果try子句没有异常发生,else子句存在的话,else子句将被执行
def compare(num1, num2):
    try:
        if (num1 >= num2):
            result = num1
        else:
            result = num2
    except:
        return "ERROR"
    else:
        print("OK")
        return result

#正确的调用
print("compare(12,5):", compare(12, 5))
#异常调用
print("compare(12,'ad'):", compare(12, 'ab'))
print("compare('12',15):", compare('12', 15))


print("try与finally语句结合使用============")
import sys
#在该Python源文件同目录下新建一个文件myfile.txt,写入内容"user-name:Jack"作为测试
try:
    #打开文件,读取第一行
    f = open('myfile.text')
    s = f.readline()
    print("result",s)
except:
    print("ERROR")
finally:
    print("close file")
#    f.close()


print("Exception万能异常==============")
import sys

try:
    #打开一个不存在的文件,将抛出异常
    f = open('file.txt')
    s = f.readline()
    print("result", s)
    #开发者清楚异常类别
#except FileNotFoundError as err:
    #不清楚异常类别,可以使用万能异常
except Exception as err:
    print("Exception-info:", err)
finally:
    print("close file")


print("主动抛出异常=================")
import sys
try:
    #输入一个文件名
    fileName = input("please input file name:")
    splitList = fileName.split('.')
    fileType = splitList[splitList.__le__()-1]
    #判断文件格式,如果不是doc则抛出异常
    if (fileType != "doc"):
        raise NameError("the file type:%s is not expected"%(fileType))
    f = open(fileName)
    s = f.readline()
    print("result", s)
except FileNotFoundError as err:
    print("Exception info:", err)
finally:
    print("close file")



