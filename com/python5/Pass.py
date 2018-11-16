# -*- coding: UTF-8 -*-
#pass语句:Python pass语句是空语句,一般用做占位符,不执行任何实际的操作,只是为了保持程序结构的完整性

#如下例子,else语句本来可以不用写,但写上更为完整,这时候pass占位的意义就体现出来了
num_set = [98, 94, 82, 67, 58, 90, 86]
for i in range(len(num_set)):
    if num_set[i] < 60:
        print("SomeOne failed!!!")
    else:
        pass