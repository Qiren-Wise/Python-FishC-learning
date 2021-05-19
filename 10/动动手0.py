i=3
mima="hzyswnpy"
while i>0:
    sr=input('请输入密码：')
    if sr==mima:
        print('密码正确，进入程序......')
        break
    elif '*' in sr:
        print('密码中不能含有"*"号！您还有',i,'次机会！',end=' ')
        continue
    elif sr!=mima:
        i-=1
        if i==0:
            print("没机会了哦....")
        else:
            print('密码输入错误！您还有',i,'次机会',end=' ')
        continue


