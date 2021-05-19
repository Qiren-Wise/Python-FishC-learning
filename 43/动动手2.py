
class Nstr:
    def __init__(self,arg = ''):
        if isinstance(arg,str):
            self.sum = 0
            for i in arg:
                self.sum += ord(i)
        else:
            print("参数错误")
            

    def __add__(self,other):
        return self.sum + other.sum

    def __sub__(self,other):
        return self.sum - other.sum

    def __mul__(self,other):
        return self.sum * other.sum

    def __truediv__(self,other):
        return self.sum / other.sum
    
    def __floordiv__(self,other):
        return self.sum // other.sum
    

a = Nstr('FishC')
b = Nstr('love')
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)