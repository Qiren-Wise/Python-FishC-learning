# 2. 要求自己写一个 MyRev 类，功能与 reversed() 相同
# (内置函数 reversed(seq) 是返回一个迭代器，是序列 seq 的逆序显示)。

class MyRev:
    def __init__(self,string):
        self.string = string
        self.length = len(string)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        self.length -= 1
        
        return self.string[self.length]

myRev = MyRev("FishC")
for i in myRev:
    print(i,end='')
