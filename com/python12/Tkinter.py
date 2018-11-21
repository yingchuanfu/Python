# -*- coding: UTF-8 -*-
#图形用户界面(GUI):控件TKinter

#窗口创建与布局
from tkinter import *
#初始化TK()
myWindow = Tk()

#设置标题
myWindow.title('Python GUI Learning')
#设置窗口大小
myWindow.geometry('400x300')
#设置窗口是否可变长 宽, True:可变;False:不可变
myWindow.resizable(width=FALSE, height=True)

#进入消息循环
myWindow.mainloop()


