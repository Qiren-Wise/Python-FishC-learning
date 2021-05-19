import urllib.request
r = urllib.request.urlopen('https://ilovefishc.com')
html = r.read(300)
print(html)