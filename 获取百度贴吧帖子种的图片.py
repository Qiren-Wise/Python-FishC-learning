from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import os

def url_open(url):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3870.400 QQBrowser/10.8.4405.400'
    }
    response = requests.get(url=url,headers=head)
    html = response.text
    return html

def get_img(html):
    count = 0
    soup = BeautifulSoup(html,'html.parser')
    reg = re.compile(r'http://.+?.jpg')
    imgList = soup.find_all('img',src=reg)
    try:
        os.mkdir("girl")
    except:
        pass

    os.chdir("girl")

    for each in imgList:
        fileName = each['src'].split('/')[-1]
        urllib.request.urlretrieve(each['src'],fileName,None)
        

if __name__ == '__main__':
    get_img(url_open('https://tieba.baidu.com/p/7130079380'))



# 做法二：小甲鱼做法
'''
import urllib.request
import re
import os

def url_open(url):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3870.400 QQBrowser/10.8.4405.400'
    }
    req = urllib.request.Request(url=url,headers=head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def get_img(html):
    reg = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    imgList = re.findall(reg,html)
    print(imgList)
    try:
        os.mkdir('girl_img')
    except:
        # 如果该文件存在则覆盖保存
        pass

    os.chdir('girl_img')

    for each in imgList:
        fileName = each.split('/')[-1]
        urllib.request.urlretrieve(each,fileName,None)


if __name__ == '__main__':
    get_img(url_open('https://tieba.baidu.com/p/7130079380'))
'''