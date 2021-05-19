import easygui as eg
import urllib.request
import chardet

def writeFile():

    urlfile = eg.fileopenbox('请选择文件',default='E:\\学习\\Python 练习\\54\\*.txt')   # 选择文件位置
    with open(urlfile) as f1:
        url = f1.read().splitlines()     # 将文本以换行符分割，url地址作为列表返回

    count = 1   # 文件尾缀默认为1
    for i in url:   # 将查到到的url地址迭代
        html = urllib.request.urlopen(i).read()

        # 获取编码
        code = chardet.detect(html)['encoding']
        if code == 'GB2312':
            code = 'GBK'

        fileName = 'url_%d' % count     # 修改文件名
        with open(r'E:\学习\Python 练习\\54\%s.txt' % fileName,'w',encoding=code) as f2:
            f2.write(html.decode(code,"ignore"))     # 打开文件并进行写入
        count += 1

if __name__ == '__main__':
    writeFile()