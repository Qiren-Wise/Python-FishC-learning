# 2. 再来一个有趣的案例：编写描述符 MyDes，使用文件来存储属性，属性的值会直接存储到对应的pickle（腌菜，还记得吗？）的文件中。
# 如果属性被删除了，文件也会同时被删除，属性的名字也会被注销。

# 我是把第二题的方式进阶了
import time
import os
import pickle

class Record:
        def __init__(self,value=None,name=None):   # 初始化需要的变量及名称
                self.val = value
                self.name = name 

        def __get__(self,instance,owner):
                # 需要设置一个文件写入操作
                self.write()
                return self.val
              

        def __set__(self,instance,value):
                self.val = value
                self.write()

        def write(self):
                self.clock = time.asctime()
                temp = self.name + '.pkl'
                with open(temp,'ab') as f:
                        binWord = "%s变量位于北京时间：%s被修改，%s=%s\n" % (self.name,self.clock,self.name,str(self.val))
                        pickle.dump(binWord,f)

class Test:
        x = Record(10,'x')
        y = Record(8.8,'y')

        def __delattr__(self,instance):
                temp = '%s.pkl' % instance
                os.remove(temp)

t = Test()
print(t.x)

print(t.y)

t.x = 5

t.y = 20
t.y = '我爱你'

del t.x



# 这是小甲鱼的做法，都一样
""" import os
import pickle
 
class MyDes:
    saved = []
 
    def __init__(self, name = None):
        self.name = name
        self.filename = self.name + '.pkl'
 
    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)
 
        with open(self.filename, 'rb') as f:
            value = pickle.load(f)
 
        return value
 
    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)
 
    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)

class Test:
    x = MyDes('x')
    y = MyDes('y')

t = Test()


t.x = 5

t.y = 20
print(t.x)

print(t.y)
t.y = '我爱你' """


                