import time
start =time.time()
rome = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
special = {4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
specialKey = [4,9,40,90,400,900]

def judge(rome,num):
    romeKey = [1,5,10,50,100,500,1000]
    if str(num)[0] == '9' or str(num)[0] == '4':
        specialRome(specialKey,num,special,new_rome)
    else:
        for each_key in reversed(romeKey):
            if num >= each_key:
                turn(each_key,num,rome,new_rome)
                break

new_rome = []

def turn(new,num,rome,new_rome):
    new_rome.append(num//new * rome[new])
    one = num % new 
    judge(rome,one)

def specialRome(specialKey,num,special,new_rome):
    for each_key in reversed(specialKey):
        if num >= each_key:
            new_rome.append(special[each_key])
            one = num % each_key
            judge(rome,one)
            break

while True:
    num = input('请输入一个整数（1-4999）：')
    try:
        num = int(num)
        if 4999 >= num > 0:
            judge(rome,num)
            break
        else:
            print('不是让你输入1-4999范围内的数嘛~再来一遍吧！')
    except (ValueError,NameError):
        print('只能输入整数哦~你又在耍什么坏心眼')


print('原数字：%s\n转换后的罗马数：' % num,end='')   
for each in new_rome:
    print(each,end='')
end = time.time()
print('\n程序执行时间: %s 秒' % round(end-start,3))