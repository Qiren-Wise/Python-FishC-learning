'''
配合 EasyGui，给“下载一只猫“的代码增加互动：
    让用户输入尺寸；
    如果用户不输入尺寸，那么按默认宽400，高600下载喵；
    让用户指定保存位置。
'''

import easygui as eg
import urllib.request

def main():
    while 1:
        try:
            width,height = eg.multenterbox('请填写喵的尺寸','下载一只喵',['宽：','高：'],[400,600])
        except TypeError:
            eg.msgbox("结束下载")
            return
        try:
            width = int(width.strip())
            height = int(height.strip())
            break
        except:
            eg.msgbox("请输入整数或退出程序！")

    response = urllib.request.urlopen('http://placekitten.com/g/%d/%d' % (width,height))
    html = response.read()
    
    fileName = eg.filesavebox('请选择存放喵的文件夹','浏览文件夹',default='*.jpg')
    
    with open(fileName,'wb') as f:
        f.write(html)

if __name__ == '__main__':
    main()


# 小甲鱼方法
'''
import easygui as g
import urllib.request
 
def main():
    msg = "请填写喵的尺寸"
    title = "下载一只喵"
    fieldNames = ["宽：", "高："]
    fieldValues = []
    size = width, height = 400, 600
    fieldValues = g.multenterbox(msg, title, fieldNames, size)
 
    while 1:
        if fieldValues == None:
            break
        errmsg = ""
 
        try:
            width = int(fieldValues[0].strip())
        except:
            errmsg += "宽度必须为整数！"
 
        try:
            height = int(fieldValues[1].strip())
        except:
            errmsg += "高度必须为整数！"    
 
        if errmsg == "":
            break
        
        fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
 
    url = "http://placekitten.com/g/%d/%d" % (width, height)
 
    response = urllib.request.urlopen(url)
    cat_img = response.read()
 
    filepath = g.diropenbox("请选择存放喵的文件夹")
 
    if filepath:
        filename = '%s/cat_%d_%d.jpg' % (filepath, width, height)
    else:
        filename = 'cat_%d_%d.jpg' % (width, height)
 
    with open(filename, 'wb') as f:
        f.write(cat_img)
 
if __name__ == "__main__":
    main()
'''