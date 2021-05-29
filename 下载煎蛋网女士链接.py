from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import base64
import re
import os
import time

img_num = 0 # 此变量用于统计下载图片数量
# 此函数用于访问网站并返回网页内容
def url_open(url):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3870.400 QQBrowser/10.8.4405.400'
    }
    req = urllib.request.Request(url,headers=head)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

# 获取网页页数
def get_page(html):
    soup = BeautifulSoup(html,'html.parser')
    page = soup.find(class_='current-comment-page').text
    page = page[1:-1]
    return page

# 进度提示  cheak为0则打印图片，反之则打印网址
def process(index=0,name='',check=1):
    global img_num
    if check:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        print('{}、进入网址：{}'.format(index,name))
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    else:
        img_num += 1
        print('正在下载第{}张图片，已命名为：{}'.format(img_num,name))
        

# 下载图片
def download_img(index,html):
    fileName = 'girl_'
    soup = BeautifulSoup(html,'html.parser')
    # 获取图片的所有标签
    img = soup.find_all('img',src=re.compile('sinaimg'))

    for each in img:
            fileName += '{}_{}'.format(index,img.index(each)) 
            # 获取图片链接
            img_url = ''.join(['http:',each['src']])
            # 打印进度
            process(name=fileName,check=0)
            img_html = urllib.request.urlopen(img_url).read()
            with open('{}.jpg'.format(fileName),'wb') as f:
                f.write(img_html)

            fileName = 'girl_'


# 获得加密网址
def secret(today,url,pageNum):

    # 日期字符+页码，利用base64进行加密
    base_page = ''.join([today,'-',str(pageNum)])
    base_page = base_page.encode('utf-8')
    base_page = base64.b64encode(base_page)

    # 融合所有内容，获得最后的网址
    url = ''.join([url,base_page.decode('utf-8'),'#comments'])
    return url

def main(folder='girl',pages = 10):
    # 切换工作目录
    os.mkdir(r'C:\Users\13326\Desktop\示例文件\images\{}'.format(folder))
    os.chdir(r'C:\Users\13326\Desktop\示例文件\images\{}'.format(folder))
    url = 'http://jandan.net/girl/'
    html = url_open(url)

    # 得到网页页码
    pageNum = int(get_page(html))

    # 获取今日的日期，用于获取加密网址
    today = ''
    for i in time.localtime()[:3]:
        today += str(i) if i >= 10 else ''.join(['0',str(i)])

    for i in range(pages):
        # 每执行一次，页码-1
        pageNum -= i
        # 获得加密网址
        url = secret(today,'http://jandan.net/girl/',pageNum)
        # 访问网址
        for_html = url_open(url)
        # 打印进度
        process(i,url)
        # 下载图片
        download_img(i,for_html)


if __name__ == '__main__':
    main()


