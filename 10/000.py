e = 0
for a in range(100,1000):
    b = a % 10   #个位数
    c = a // 10 % 10    #十位数
    d = a // 100      #百位数
    if b ** 3 + c ** 3 + d ** 3 == a:  #判断条件
        e += 1
print(e) 
