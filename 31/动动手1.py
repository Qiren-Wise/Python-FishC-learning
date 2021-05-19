first = input(r'请输入待查找的初始目录：')
target = input('请输入需要查找的目标文件：')
import os
def find(first,target):
    os.chdir(first)     # 定义工作目录为指定文件夹下
    
    for each in os.listdir(os.curdir):  # 将当前文件夹下的所有文件/文件夹都查找出来进行循环
        if each == target:      # 当循环的目标和目标文件相同时
            print(os.getcwd() + os.sep + each)      # 输出路径
        if os.path.isdir(each): # 如果each时个文件夹的话
            find(each,target)   # 使用递归，把each这个参数传到first的位置，这样通过第5行内容重新定义工作文件夹
            os.chdir(os.pardir) # 切记返回上一级目录！


find(first,target)  