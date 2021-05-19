# 0. 要求实现一个功能与 reversed() 相同（内置函数 reversed(seq) 是返回一个迭代器，是序列 seq 的逆序显示）的生成器。

def myRev(string):
    index = len(string)
    for i in range(index-1,-1,-1):
        yield string[i]

for j in myRev("fishc"):
    print(j,end='')
    
