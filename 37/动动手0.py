# %%
#我的方法
class Person:
    name = '小甲鱼'
    def put(self,name):
        self.name = name
        print("%s" % self.name)
# %%
#小甲鱼方法
class Person:
    name = '小甲鱼'
    
    def printName(self):
       print(self.name) 