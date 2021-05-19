#查找子字符串在目标字符串中出现的次数
def a(x,y):                 #定义函数
    count = 0               #次数为0
    chang = len(x)          #获取长度
    if y not in x:          #先打印无子字符串时候的结果
        print('目标字符串中无子字符串。')
    else:
        for each in range(chang-1):             #循环的长度
            if x[each] == y[0]:                 #如果目字符串的第each个字符在y的第0个字符中
                if x[each+1] == y[1]:           #与上同理
                    count += 1                  #次数+1
        print('字符串在目标字符串中出现了%d次' % count)         
        #打印和输入字符串！
x = input('请输入字符串：')
y = input('请输入子字符串(至少2字符）：')
a(x,y)

