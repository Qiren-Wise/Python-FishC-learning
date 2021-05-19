fileName = input(r'请输入要打开的文件(C:\\text.txt):')
rows = input('请输入需要显示的行数【格式如13:21 或 :21 或 21:】：')
def filePrint(fileName,rows):
    (one,two) = rows.split(':')     # 把冒号两边的值分别给one和two
    
    if one == '':
        one = 1         # 定义它们时空值的情况
    if two == '':
        two = -1

    if one == 1 and two == -1:      # 如果冒号两边都是空值，即':'时
        middle = '的全文'
    elif one == 1:                  # 如果冒号左边时空值，即':21'时
        middle = '从开头到第%s行的内容' % two
    elif two == -1:                 # 如果冒号右边时空值，即'21:'时
        middle = '从第%s行到结尾的内容' % one
    else:                           # 如果冒号两边都有值，即'13:21'时
        middle = '从第%s行到第%s行的内容' % (one,two)

    print('\n文件%s%s如下:\n' % (fileName,middle))      # 依据上面的if语句可得出输入的是第几行到第几行，这里打印出来

    begin = int(one) - 1        # 因为最终打印的时候是需要打印begin行本身的，所有先减一
    end = int(two)              # 把end转换成数值
    lines = end - begin         # 获取需要打印的行数
    f = open(fileName)          # 打开文件

    for i in range(begin):      # 把begin行前面的行消耗掉，指针随之移到后面
        f.readline() 

    if lines < 0:               # 如果行数小于0，说明需要打印全文
        print(f.read())  
    else:
        for i in range(lines):  # 因为前面已经把指针移后了，所有现在直接打印需要的行数就好了
            print(f.readline(),end='')
    
    f.close()

filePrint(fileName,rows)         

