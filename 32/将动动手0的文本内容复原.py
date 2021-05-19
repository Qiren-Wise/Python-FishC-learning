import pickle
import os

file_name = r'D:\学习\Python 练习\\32'
def again(file_name):
    os.chdir(file_name)

    for each in os.listdir(os.curdir):
        if os.path.splitext(each)[1] == '.pkl':
            f = open(each,'rb')
            print('文件%s的内容是：' % each)
            content = pickle.load(f)
            for each_file in content:
                print(each_file)
            print('=============================================================')
            
again(file_name)