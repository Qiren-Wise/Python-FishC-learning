#十进制转二进制(除2取余)
'''
除2取余：转换89
89 / 2 = 44 ..... 1
44 / 2 = 22 ..... 0
22 / 2 = 11 ..... 0
11 / 2 = 5 ...... 1
5 / 2 = 2 ....... 1
2 / 2 = 1 ....... 0
1 / 2 = 0 ....... 1
从下往上数，即89 -> 1011001
'''

def a(x):
    '先设置一个函数'
    list1 = []          #创建一个空列表方便把后面各个元素添加进去
    str1 = ''           #空字符串可以把上面列表的值合在一起

    while x:
        i = x%2             #把余数取出来放在一个变量内
        x = x//2            #用地板除的方法可以把他们的差求出来进行下一次除数运算（地板除可以没有小数点）
        list1.append(i)     #把取出来的余数放到列表内

    while list1:
        str1 += str(list1.pop())        #把列表内的元素取出来放到空字符串内。

    return str1

print(a(89))
        

