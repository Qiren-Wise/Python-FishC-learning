import os
first = input(r'请输入待查找的初始目录：')
format = ['.mp4','.rmvb','.avi']
afirst = os.getcwd()
def find(first,format):
    os.chdir(first)     # 定义新的工作目录
    
    for each in os.listdir(os.curdir):      # 将工作目录中的文件进行for循环
        if os.path.splitext(each)[1] in format:     # 如果文件的后缀名是format列表里的后缀
            f_write = open(r'%s\vedioList.txt' % afirst,'a')    # 打开文件      
            f_write.write(os.getcwd() + os.sep + each)      # 写入路径
            f_write.write('\n\n')   
            f_write.close()     # 关闭文件
        if os.path.isdir(each):     # 如果该文件不是format列表中的后缀的话，就看它是不是一个文件夹
            find(each,format)       # 是文件夹就利用递归，把工作目录重新定义以下，然后查找里面的文件
            os.chdir(os.pardir)     # 切记要返回上一层目录
    
find(first,format)   

# 以下是小甲鱼写的代码
'''
import os
 
def search_file(start_dir, target) :
    os.chdir(start_dir)     # 定义新的工作目录
    
    for each_file in os.listdir(os.curdir) :        # 将工作目录中的文件进行for循环
        ext = os.path.splitext(each_file)[1]
        if ext in target :      # 如果文件的后缀名是target列表里的后缀
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)    # 将内容写入到列表中
        if os.path.isdir(each_file) :       # 如果该文件不是target列表中的后缀的话，就看它是不是一个文件夹
            search_file(each_file, target) # 是文件夹就利用递归，把工作目录重新定义以下，然后查找里面的文件
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录
 
start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()
 
target = ['.mp4', '.avi', '.rmvb']
vedio_list = []     # 定义循环时用于写入内容的列表
 
search_file(start_dir, target)
 
f = open(program_dir + os.sep + 'vedioList.txt', 'w')       # 打开文件
f.writelines(vedio_list)        # 将列表中的文件写入到f的每一行中
f.close()       # 关闭文件
'''       

            