from easygui import *
import os
import time
#suffix = ['c','js','py','html']
house = diropenbox('请选择您的代码库')
start = time.time()
row = {'c':0 ,'js':0 ,'py':0 ,'html':0}
count = {'c':0 ,'js':0 ,'py':0 ,'html':0}

def rowCount(name,suffix,count):
    with open(name,encoding='utf-8') as f:
        count[suffix] += 1
        for i in f:
            if i.strip() != '':
                row[suffix] += 1


def find(house,row):
    os.chdir(house) # 定义选择的文件夹为工作文件夹
    show = os.listdir(os.curdir)    # 把文件夹中的文件和目录放到列表中
    for each in show:
        if os.path.isfile(each):
            suffix = each.rsplit('.',1)[1]
            if suffix in row:
                rowCount(each,suffix,count) # 函数一   
              
        if os.path.isdir(each):
            find(each,row)
            os.chdir(os.pardir)

def test(row,count):
    sum = row['c'] + row['js'] + row['py'] + row['html']
    plan = str(round(sum/100000*100,2)) + '%'
    cha = 100000 - sum
    name = ['c','js','py','html']
    if sum < 100000:
        msg = ('你目前共累计编写了%d行代码，完成进度：%s\n离10万行代码还差%d行，请继续努力！' % (sum,plan,cha))   
        text = '【.%s】源文件%d个，源代码%d行\n【.%s】源文件%d个，源代码%d行\n【.%s】源文件%d个，源代码%d行\n【.%s】源文件%d个，源代码%d行' % (name[0],count['c'],row['c'],name[1],count['js'],row['js'], \
                name[2],count['py'],row['py'],name[3],count['html'],row['html'])
    textbox(msg,'统计结果',text)

find(house,row)
test(row,count)
end = time.time()
msg = '本次程序运行时间：%s 秒' % (end-start)
msgbox(msg)
