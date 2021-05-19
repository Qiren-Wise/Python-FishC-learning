# power(x, y) 为计算并返回 x 的 y 次幂的值。
'''
解释：
power(2,3) = 2*power(2,2) 
power(2,2) = 2*power(2,1)
power(2,1) = 2*power(2,0)
power(2,0) = 1
'''
def power(x,y): 
    if y:       
        return x * power(x,y-1)         #如果y不等于0，那么x就会乘y-1的值，执行3次，就乘3次2,如上解释。
    else:
        return 1        #最后y等于0时返回1，那么结果就会乘1，还是原来的值。

print(power(2,3))

