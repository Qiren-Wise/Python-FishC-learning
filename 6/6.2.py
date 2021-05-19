nian=input("请输入年份：")
while not nian.isdigit():
    nian = input("请重新输入：")

a = int(nian)
if a%400 == 0 and a%1000 == 0:
    print("这是闰年")
else:
          if a%4 == 0 and a/100 != int(a/100):
              print("这是闰年")
          else:
              print("这是平年")

    
