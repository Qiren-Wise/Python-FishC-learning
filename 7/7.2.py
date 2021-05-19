x=7
i=1
jie=1

while i<=2:
    if x%2==1 and x%3==2 and x%5==4 and x%6==5:
        jie=1
    else:
        x=7*(i+1)
    i+=1

if jie == 1:
    print("阶梯数是：",x)
else:
    print("找不到答案")
