
import time
start=time.time()
i=0

while i!=1:
    cj=int(input("请输入一个数："))
    if 90<=cj<=100:
        print("A")
        i=1
    elif 80<=cj<90:
        print("B")
        i=1
    elif 60<cj<80:
        print("C")
        i=1
    elif cj<=60:
        print("D")
        i=1
    else:
        print("输入错误")
        
end=time.time()
print('Running time: %s Seconds'%(end-start))