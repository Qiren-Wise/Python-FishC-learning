x = str(input('请输入一句话：'))
y = x[::-1]
if y == x:
    print('是回文联') 
else:
    print('不是回文联')

'''
使用函数：
def a(x):
    list1 = list(x)
    list2 = list(reversed(x))  
    if list1 == list2:
        print('是回文联')
    else:
        print('不是回文联')
    
x = input('请输入一句话：')
a(x)
思路：先把x里面的值转换为列表，然后再用列表翻转，即list(reversed(x)),这样，如果list1和list2相等，就是回文联了
'''