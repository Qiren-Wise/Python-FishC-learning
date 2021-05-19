while True:
    zs = input('请输入一个整数(输入Q结束程序):')
    if zs != 'Q':
        zs = int(zs)
        print('十进制 -> 十六进制 ：%d -> 0x%x' % (zs,zs))
        print('十进制 -> 八进制 ：%d -> 0o%o' % (zs,zs))
        print('十进制 -> 二进制 ：%d ->' % (zs),bin(zs))
    else:
        break

        

    