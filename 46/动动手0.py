class Prompt:
    def __getattr__(self,name):
        print("该属性不存在")

p = Prompt()
p.x