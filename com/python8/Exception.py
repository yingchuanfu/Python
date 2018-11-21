# -*- coding: UTF-8 -*-
print("自定义异常====================")
#自定义异常:通过直接继承或者间接继承Exception类,来创建自己的异常

#自定义异常,继承Exception
class MyException(Exception):
    def __init__(self, *args):
        self.args = args
try:
    raise MyException("the file type is not expected")
except MyException as err:
    print(err)
#上面的例子中,类Exception默认的__init__()被覆盖


#创建一个模块有可能抛出多种不同的异常时,一种通常的做法是为这个包建立一个基础异常类
#然后基于这个基础类为不同的错误情况创建不同的类

#如下实例:
#创建一个基础异常类
class MyException(Exception):
    def __init__(self, *args):
        self.args = args
#定义不同种类的业务异常,继承基础异常类
class loginError(MyException):
    def __init__(self, code = 100, message =  'login error',
                 args =('Internal Server Error','http:500')):
        self.args = args
        self.message = message
        self.code = code

class loginOutError(MyException):
    def __init__(self):
        self.args = ('Internal Server Error')
        self.message = 'login out error'
        self.code = 200
#raise loginError(),使用默认参数
try:
    raise loginError()
except loginError as e:
    print(e) #输出异常
    print(e.code) #输出错误代码
    print(e.message) #输出错误信息

#raise loginError(),传入参数
try:
    raise loginError(400, 'password is wrong!',('Internal Server Error',))
except loginError as e:
    print(e) #输出异常
    print(e.code) #输出错误代码
    print(e.message) #输出错误信息