# -*- coding: UTF-8 -*-
#条件 循环及其它语句

#while循环:与for循环不同,其循环的依据是条件判断
#while语法:当condition为True,则执行Action,否则退出
#while Condition:
#    Action

print("实例1:求一组数据的平均值==================")
num_set = [98, 94, 82, 67, 58, 90, 86]
sumOfNum = 0
index = 0

while index < len(num_set):
    sumOfNum += num_set[index]
    index += 1
    #求平均值并打印结果
    average = sumOfNum / len(num_set)
    print("The average is:%f"%(average))