def contrast(one,two):
    f1 = open(one)
    f2 = open(two)
    rows = 0
    differ = []

    for each_one in f1:
        rows += 1
        each_two = f2.readline()
        if each_one != each_two:
            differ.append(rows)
    
    f1.close()
    f2.close()
    return differ

one = input('请输入需要比较的头一个文件名：')
two = input('请输入需要比较的另一个文件名：')

difference = contrast(one,two)
if len(difference) == 0:
    print('两个文件完全一样！')
else:
    print('两个文件共有【%d】处不同：' % len(difference))
    for each in difference:
        print('第%d行不一样' % each)

            


