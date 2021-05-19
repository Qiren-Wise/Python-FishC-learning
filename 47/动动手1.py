# 1. 按要求编写描述符 MyDes：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件：record.txt

import time
import os

class Record:
        def __init__(self,value=None,name=None):   # 初始化需要的变量及名称
                self.val = value
                self.name = name
                self.count = 0  

        def __get__(self,instance,owner):
                # 需要设置一个文件写入操作
                self.write()
                return self.val
              

        def __set__(self,instance,value):
                self.val = value
                self.write()

        def write(self):
                self.clock = time.asctime()
                if ('a.txt' in os.listdir() and self.count<1):
                        self.count += 1
                        os.remove('a.txt')

                with open('a.txt','a',encoding='utf-8') as f:
                        f.write("%s变量位于北京时间：%s被修改，%s=%s\n" % (self.name,self.clock,self.name,str(self.val)))

class Test:
        x = Record(10,'x')
        y = Record(8.8,'y')

t = Test()
print(t.x)

print(t.y)
time.sleep(1)
t.x = 5

t.y = 20
t.y = '我爱你'

                