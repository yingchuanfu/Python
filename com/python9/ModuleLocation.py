# -*- coding: UTF-8 -*-
#模块的位置
print("1将模块放置于正确的位置================")
#通过下面的代码,打印搜索路径
import sys

for temp in sys.path:
    print(temp)