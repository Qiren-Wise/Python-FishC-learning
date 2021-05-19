class Example:
    def __init__(self,*content):
        
        if not content:
            print("并没有传入参数")
        else:
            print("传入了",len(content),"个参数,","分别是：",*content)

a = Example()

