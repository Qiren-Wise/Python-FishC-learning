import pickle
file_name = r'D:\学习\Python 练习\\32\record.txt'
def split(file_name):       # 函数一    将文件中的各个内容分割开，并用列表保存
    f = open(file_name,encoding='utf-8')    # 打开文件
    boy = []
    girl = []
    count = 1

    for each in f:  # 循环f文件中的每一行
        if each[:6] != '======':    # 如果前六个字符都是'======'
            (role,content) = each.split(':',1)  # 将角色和内容分开，以':'为界
            if role == '小甲鱼':
                boy.append(content)     # boy列表输入小甲鱼的内容
            if role == '小客服':
                girl.append(content)    # girl列表输入小客服的内容
        else:
            write(boy,girl,count)      # 运行函数二
            count += 1      # 每循环一次count+1，然后文件名后面的数字也会+1
            boy = []
            girl = []

    f.close()
    write(boy,girl,count)   # 因为原文件中最后一段时没有'======'的，所有需要额外运行一次函数

def write(boy,girl,count):      # 函数二 创建文件和写入文件内容 
    file_name_boy = 'boy_' + str(count) + '.pkl'    # 定义函数名，利用前面count变量区别每个文件
    file_name_girl = 'girl_' + str(count) + '.pkl'

    boy_file = open(r'D:\学习\Python 练习\\32\%s' % file_name_boy,'wb')     # 利用'wb'模式打开文件
    girl_file = open(r'D:\学习\Python 练习\\32\%s' % file_name_girl,'wb')

    pickle.dump(boy,boy_file)       # 将文本boy列表中的内容倒入打开的文件中
    pickle.dump(girl,girl_file)

    boy_file.close()    
    girl_file.close()

split(file_name)