import os
import re
 
def search(keys,first):
    os.chdir(first)
    row = 0

    for each in os.listdir(os.curdir):
        if os.path.isfile(each):
            target = open(each,encoding='utf-8')
            for each_file in target:
                row += 1
                position = []
                if keys in each_file:
                    f = re.finditer(keys,each_file)
                    for i in f:
                        position.append(i.span()[0])
                    print('在文件' + os.getcwd() + os.sep + each + '中找到关键字%s:' % keys)
                    print('关键字出现在第%s行，第%s个位置' % (row,position))
                    print('====================================')
        else:
            search(keys,each)
            os.chdir(os.pardir)

keys = input('请将该脚本放于待查找的文件夹内，请输入关键字:')
ask = input('请问是否需要打印关键字【%s】在文件中的具体位置(YES/NO):' % keys)
first = os.curdir
if ask in ['YES','yes','Yes']:
    print('====================================')
    search(keys,first)


'''
这是小甲鱼的方法
import os

def print_pos(key_dict):    # 函数四    把关键字出现的位置打印出来，通过字典的键和值
    keys = key_dict.keys()      # 获取字典每一个键
    keys = sorted(keys) # 由于字典是无序的，我们这里对行数进行排序
    for each_key in keys:   # 循环字典的每一个键
        print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key, str(key_dict[each_key]))) # 打印
 
 
def pos_in_line(line, key):     # 函数三    如果函数二查找关键字在该文本中的话，查找每一行中的具体位置
    pos = []        # 这里的line是函数二传过来的那一行字符串
    begin = line.find(key)      # 先查找第一个字符串中关键字开始的位置
    while begin != -1:  # find没查找到会返回-1
        pos.append(begin + 1) # 用户的角度是从1开始数
        begin = line.find(key, begin+1) # 从下一个位置继续查找
 
    return pos
 
 
def search_in_file(file_name, key):     # 函数二    打开由函数一的路径找出的文件，记录行数，并且查找关键字
    f = open(file_name,encoding='utf-8')    # 函数一把路径穿过来，并打开
    count = 0 # 记录行数
    key_dict = dict() # 字典，用户存放key所在具体行数对应具体位置
    
    for each_line in f:     # 循环文本中的每一行
        count += 1      # 每循环一次，行数+1
        if key in each_line:    # 如果关键字在那一行中，运行函数三
            pos = pos_in_line(each_line, key) # key在每行对应的位置
            key_dict[count] = pos   # 字典的键是行数，字典的值时函数三返回的值
    
    f.close()
    return key_dict     # 返回key_dict并执行函数四
 
 
def search_files(key, detail):    # 函数一  找出后缀时.txt的文件及它的路径
    all_files = os.walk(os.getcwd())    # 利用walk方法把当前文件夹所有子目录和文件用三元组的方式返回
    txt_files = []      # 定义一个空目录，用于存放.txt文件的路径名
 
    for i in all_files:     # 循环每个三元组
        for each_file in i[2]:      # 查询一个三元组的第三个元素，就是它们的文件
            if os.path.splitext(each_file)[1] == '.txt': # 根据后缀判断是否文本文件
                each_file = os.path.join(i[0], each_file)   # 如果时文本文件就把路径名和文件名组合
                txt_files.append(os.path.join(i[0], each_file))     # 然后添加到存放路径名的列表中
    
    # 到这已经把路径中所有是文本文件的路径找出来了
    for each_txt_file in txt_files:     # 循环各个文本文件路径
        key_dict = search_in_file(each_txt_file, key)   
        # 函数二search_in_file的第一个参数file_name被替换成了each_txt_file       
        if key_dict:    # 如果key_dict有值
            print('================================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))  # 打印
            if detail in ['YES', 'Yes', 'yes']:
                print_pos(key_dict)     # 如果用户输入yes，就执行函数四
 
 
key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
search_files(key, detail)
'''