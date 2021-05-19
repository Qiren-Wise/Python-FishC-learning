from easygui import *
import os

way = fileopenbox('请查找显示的文本',default='*.txt')
print(way)
with open(way,encoding='utf-8') as file_name:
        txt = file_name.read()
        title = os.path.basename(way)
        msg = ('文件【%s】的内容如下：' % title)
        textbox(msg,title,txt)

