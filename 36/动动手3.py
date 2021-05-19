from easygui import *
import os

way = fileopenbox('请查找显示的文本',default='*.txt')
print(way)
with open(way,encoding='utf-8') as file_name:
        txt = file_name.read()  # 此时的txt是原内容
        title = os.path.basename(way)
        msg = ('文件【%s】的内容如下：' % title)
        t = textbox(msg,title,txt)    # 现在的t是原内容的基础上，增加或不增加的内容

def cover(t,txt,way):   # 覆盖保存
        with open(way,'w',encoding='utf-8') as file_name:
                file_name.write(t)    # 将新内容全部输入到原文件中就好

def saveAs(t,txt,way):
        new_way = filesavebox(default='*.txt')
        if os.path.splitext(new_way)[1] != '.txt':
                new_way += '.txt'
        with open(new_way,'w',encoding='utf-8') as file_name:
                file_name.write(t)

if t != txt:
        conserve = buttonbox('检测到文件内容发生改变，请选择以下操作','警告',['覆盖保存','放弃保存','另存为...'])
        if conserve == '覆盖保存':
                cover(t,txt,way)

        if conserve == '另存为...':
                saveAs(t,txt,way)
        

