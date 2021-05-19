class MyDes:
    def __init__(self,value=None,name=None):
        self.val = value
        self.name = name
    
    def __get__(self,instanse,owner):
        print("正在获取变量：%s" % self.name)
        return self.val
        
    def __set__(self,instanse,value):
        print("正在设置变量：%s" % self.name)
        self.val = value

    def __delattr__(self,instanse):
        print("正在删除变量：%s" % self.name)
        print("噢~这个变量没法删除~")

class Test:
    x = MyDes(10,'x')

t = Test()
print(t.x)
y = t.x

