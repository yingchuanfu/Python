# -*- coding: UTF-8 -*-
#break语句:用于跳出for和while循环体,也就意味着循环结束

#初始化测试数据
num_set = [98, 94, 82, 67, 58, 90, 86]
for i in range(len(num_set)):
    if num_set[i] < 60:
        print("SomeOne failed!")
        break
    else:
        print(num_set[i])

#实际应用中,break语句经常和while语句结合使用,当条件满足的时候跳出循环
while True:
    a = input("Please enter number:")
    if int(a) > 100:
        print("error!!!")
        break
    else:
        print(a)