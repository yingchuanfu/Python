# -*- coding: UTF-8 -*-
#continue语句:与break不同,continue不会退出循环体,而是跳过当前循环块的剩余语句,继续下一轮循环

print("遍历数据集,遇到小与60的数据打印提示================")
#初始化测试数据
num_set = [98, 94, 82, 67, 58, 90, 86]
for i in range(len(num_set)):
    if num_set[i] < 60:
        print("SomeOne failed!!!")
        continue
    print(num_set[i])