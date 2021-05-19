temp = input("请输入一个整数：")
shu = int(temp)
while shu:
    i = shu - 1
    while i:
        print(" ", end ="")
        i = i-1
    j = shu
    while j:
        print("*",end = "")
        j=j-1
    print()
    shu=shu - 1
