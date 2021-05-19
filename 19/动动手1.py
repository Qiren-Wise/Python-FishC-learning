#求水仙花数，如：153 = 1^3+5^+3^3
def a():
    for i in range(100,999):
        gewei = i %100 %10
        shiwei = i //10 %10 
        baiwei = i //100
        if (gewei**3)+(shiwei**3)+(baiwei**3) == i:
            print(i,end=' ')
            
print("所有的水仙花数分别是：", end='')
a()