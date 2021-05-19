def fileName(name):
    f = open(name,'w')
    print('请输入内容【单独输入\':w\'保存退出】：')

    while True:
        userInput = input()
        if userInput != ':w':
            f.write('%s\n' % userInput)
        else:
            break
        
    f.close()

name = input('请输入文件名:')
fileName(name)