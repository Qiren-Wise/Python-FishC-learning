def a(*x,base=3):               #定义函数以及其中的收集参数和题目要求的基数3
    result = 0                  #先预设结果为0
    for i in x:                 #利用for循环把x里面的每个数都相加
        result += i 

    result *= base              #最后把结果乘基数

    print('结果是：',result)

print(a(1,2,3,4,5,base=5))
