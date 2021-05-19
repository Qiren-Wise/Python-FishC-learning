# 斐波那契数列-递归实现过程
def f(n):
    if n<1:
        print('输入错误！')
        return -1
    
    if n > 2:
        return f(n-1) + f(n-2)
    else:
        return 1 

n = int(input('请输入月份：'))
result = f(n)
if result != -1:
    print('第%d月份诞生了%d只兔子' % (n,result))