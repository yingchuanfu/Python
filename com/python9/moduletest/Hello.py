#Hello.py模块代码,打印hello world!
print("hello word!!!")

def printInfo():
    print("this is my Python module code")
#__name__属性仅在该模块自身运行时执行
if __name__ == '__main__':
    print('native')
else:
    print('external(外部的)')

def printSum(x, y):
    print(x+y)


print("__all__变量======================")
#内部函数,不期望被导出
def __fun__():
    print("测试内部函数")
#通过__all__变量定义模块的公有接口
__all__ = ['printInfo','printSum']