def count(*x):                      #因为有可能有多个参数，所以定义一个收集参数
    length = len(x)                 #先获取参数的总长度
    for i in range(length):         #第一个循环是表明循环次数
        English = 0
        math = 0                    #4—7行先把各类数据归为0
        space = 0
        other = 0
        for each in x[i]:           #利用x[i]来统计每一个字符出现的样子，i代表次数
            if each.isalpha():
                English += 1
            elif each.isdigit():    #这些都是基本的if语句，'.'后面什么意思参考书本P51
                math += 1 
            elif each.isspace():
                space += 1
            else:
                other += 1
        print('第%d个字符串共有：英文字母%d个，数字%d个，空格%d个，其他字符%d个。' % (i+1,English,math,space,other))

count('I love fishC.com','I love you,you love me.')


