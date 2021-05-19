# 使用递归编写一个函数，利用欧几里得算法求最大公约数
# 欧几里得算法解释可看：while利用欧几里得算法查找最大公约数.py
def gcd(x,y):
    if y:
        return gcd(y,x%y)       #如果y不等于0时，原来y的位置就替换为x%y，即他们的余数，并且把x换成原来的y
    else:
        return x        #当y约为0了，返回x的值

print(gcd(12,16))