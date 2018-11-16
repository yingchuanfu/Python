# -*- coding: UTF-8 -*-
#条件 循环及其它语句

#python for循环语句:遍历序列中的项目,这里序列包括但不限于字符串 列表 元组 字典
#语法for <item> in <sequence>:
#    <actions>
#当 <item> in <sequence>为True时,执行<actions>

#实例1:求一组数据的平均值
#测试数据集
num_set = [98, 94, 82, 67, 58, 90, 86]
sumOfNum = 0
#遍历列表中的元素,求和
for element in num_set:
    sumOfNum += element
#求平均值并打印结果
average = sumOfNum / len(num_set)
print("The average is:%f"%(average))

print("实例2:通过range()函数遍历数据序列=========================")
#1.range(n):生成步长为1的数列:1,2,3 ...n;
#2.range(m,n):生成步长为1的数列:m, m+1,m+2,...,n;
#3.range(m,n,s):生成步长为s的数列:m, m+s, m+2s,...,X(x<=n)
for index in range(4):
    print("index:",index)

print("实例3:for循环结合range()遍历数据序列=====================")
#测试数据集
city_set = ['BeiJin', 'TianJin', 'ShangHai', 'HangZhou', 'SuZhou']
#索引从0开始,以步长2遍历
for index in range(0, len(city_set), 2):
    print("city_set[%d]:%s"%(index, city_set[index]))