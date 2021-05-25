import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re



def main() -> None:
    while 1:
        try:
            name = input('请输入关键词("q!退出")：')
            assert(name)   # 如果用户输入控制，断言报错 
            if name == 'q!':  
                return
            break
        except:
            print('请重新输入("q!退出")')
    name = urllib.parse.quote(name)
    
    # 访问网站
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    url = ''.join(['https://baike.baidu.com/item/',name,'?force=1'])
    
    req = urllib.request.Request(url,headers=head)
    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html,'html.parser')


    for i in soup.find_all(href=re.compile('view')):
        if i.text in ['多义词','义项']:
            print('{} -> https://baike.baidu.com{}'.format(i.text,i['href']))

    moreWord = soup.find_all(attrs={'data-lemmaid':True},href=re.compile('item'))
    try:
        assert(len(moreWord))
    except:
        print('未查找到对应词条')
        return

    print("共{}个义项 -> {}".format(len(moreWord),url))
    for i in moreWord:
        temp = i.text.split('：')
        print("{}（{}） -> https://baike.baidu.com{}".format(temp[0],temp[1],i['href']))



if __name__ == '__main__':
    main()