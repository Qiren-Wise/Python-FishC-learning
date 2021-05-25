import urllib.request
from bs4 import BeautifulSoup
import re

def main():
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    url = 'http://baike.baidu.com/view/284853.htm'

    req = urllib.request.Request(url,headers=head)

    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html,'html.parser')
    tag = soup.find_all(href=re.compile("item"))


    for i in tag:
        print('%s -> ' % i.text , ''.join(['https://baike.baidu.com',i['href']]))

if __name__ == '__main__':
    main()