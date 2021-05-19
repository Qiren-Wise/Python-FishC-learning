import os
def stat(file_name):        
    f = os.listdir(file_name)       # 把file_name目录中的所有文件用列表的形式赋值给f
    length = len(f)         # 获取f的长度
    one = []

    for each in range(length):
        name = os.path.splitext(f[each])    # 让f列表中的文件名和后缀名利用splitext()方法分开
        one.append(name[1])     # 把其中的后缀名添加到one中
    
    two = set({})   # 因为我们查找文件名不需要重复的文件名，所有用集合
    count = 0

    for each_one in range(len(one)):
        two.add(one[each_one])      # 把所有后缀名添加到集合中去

    for each_two in two:  
        names = each_two   # 把集合中的每一个值都赋给names
        count = one.count(names)    # 读取列表中名为names的次数
        print('该文件下共有类型为【%s】的文件%d个' % (names,count))     # 打印后缀名和次数


file_name = r'D:\学习\Python 练习\\24、25'
stat(file_name)

# 以下是小甲鱼写的代码
'''
import os
 
all_files = os.listdir(os.curdir) # 使用os.curdir表示当前目录更标准
type_dict = dict()
 
for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹', 0)
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1
 
for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))
'''
                



    
        
