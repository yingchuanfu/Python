# -*- coding: UTF-8 -*-
#数据结构:队列(queue):即"先进先出",就像排队打饭,队头的人先打到饭,队尾的人最后

from collections import deque
#基于列表初始化一个队列
queue = deque(['A', 'B', 'C'])
#队尾添加元素
queue.append('D')
print('queue', queue)
#队头出列
queue.popleft()
print('queue', queue)

queue.popleft()
print('queue', queue)