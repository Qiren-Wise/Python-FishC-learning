import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容：')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}


data = {
    'i':content,
    'from':'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15880623642174',
    'sign': 'c6c2e897040e6cbde00cd04589e71d4e',
    'ts': '1588062364217',
    'bv': '42160534cfa82a6884077598362bbc9d',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom':'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url,data,head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

target = json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

# 以下代码感谢：码农一号已就位 提供的资源
# https://blog.csdn.net/xdc1812547560/article/details/108031237
