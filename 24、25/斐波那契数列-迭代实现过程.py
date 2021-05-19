# 斐波那契数列-迭代实现过程
def f(n):
    a1 = 1
    a2 = 1
    a3 = 1
    if n<1:
        print('输入有误！')
        return -1

    while n>2:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        n -= 1

    return a3

n = int(input('请输入月份：'))
result = f(n)
if result != -1:
    print('第%d月份诞生了%d只兔子' % (n,result))