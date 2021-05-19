one = input('请输入要打开的文件(C:\\\\text.txt):')
rows = int(input('请输入需要显示该文件前几行：'))
def filePrint(one,rows):
    f1 = open(one)
    count = 0
    print('文件%s的前%d行的内容如下：\n' % (one,rows))

    for each_one in f1:
        count += 1
        if count <= rows: 
            print(each_one)
        else:
            break
    

filePrint(one,rows)
    

