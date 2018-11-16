# -*- coding: UTF-8 -*-
#条件 循环及其它语句

#条件控制语句if-else
A = 1
B = 5
if A >= B:
    print('the larger number is:', A)
else:
    print('the larger number is:', B)

#实例1:从控制台输入两个数字A,B,判断大小后输出较大的数字,如果相等则输出提示和数值
#从控制台输入数据默认为字符串类型,需要强制转换为int类型

A = (input("Please enter the number A:"))
B = (input("Please enter the number B:"))
if A > B:
    print('the larger number is:', A)
elif A == B:
    print('A and B are equal to', A)
else:
    print('the larger number is:', B)

print("实例2:从控制台输入学号,如果学号正确则输出考试成绩;如果学号有误,输出报错提示")
#创建一个"学号-成绩"
exam_results = {'2018002':95, '2018013':'90', '2018023':85}
#接收从控制台输入的学号,默认为字符串类型
stu_num = input("Please enter the student number:")
#删除输入学号首尾空格,避免影响查询
stu_num = stu_num.strip()
#判断输入的学号是否存在于"学号-成绩"字典中
if stu_num in exam_results.keys():
    print('Your score is:', exam_results.get(stu_num))
else:
    print('The student number you entered is incorrect!')