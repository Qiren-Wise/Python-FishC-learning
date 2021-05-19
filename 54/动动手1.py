import urllib.request
import chardet

def main():
    url = input("请输入URL：")
    html = urllib.request.urlopen(url).read()
    # 识别网页编码
    code = chardet.detect(html)['encoding']
    if code == 'GB2312':    # 如果是GB2312就转换位GBK，因为GBK支持向下兼容
        code = 'GBK'
    
    print('该网页使用的编码是：%s' % code)


if __name__ == "__main__":
    main()

