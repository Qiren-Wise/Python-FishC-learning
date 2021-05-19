def count(*x):
    length = len(x)
    for i in range(length):
        English = 0
        math = 0
        space = 0
        other = 0
        for each in x[i]:
            if each.isalpha():
                English += 1
            elif each.isdigit():
                math += 1 
            elif each.isspace():
                space += 1
            else:
                other += 1
        print('第%d个字符串共有：英文字母%d个，数字%d个，空格%d个，其他字符%d个。' % (i+1,English,math,space,other))

count('I love fishC.com','I love you,you love me.')


