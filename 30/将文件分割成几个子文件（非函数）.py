count = 1
boy = []
girl = []

f = open(r"C:\Users\13326\Desktop\示例文件\record2.txt")

for each_line in f:
    if each_line[:6] != "======":               # 如果前六个字符不是'======'的话
        (role,line_spoken) = each_line.split('：',1)         # .split可以以':'为分隔符，把值分别赋给role和line_spoken
        if role == '小甲鱼':
            boy.append(line_spoken)             # 如果冒号前面的值是小甲鱼的话，把冒号后面的是添加到boy这个列表中。下面同理。
        if role == '小客服':
            girl.append(line_spoken)
    else:
        file_name_boy = 'boy_' + str(count) + '.txt'        # 如果前六个字符等于'======'时，就把文件名字符串赋值给file_name_boy
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy,'w')      # 以写入的方式打开file_name_boy文件
        girl_file = open(file_name_girl,'w')

        boy_file.writelines(boy)                # 将刚刚添加到列表boy中的内容写入到boy_file中去
        girl_file.writelines(girl)
        
        boy = []                                # 重置这个列表，好让下一次循环没有重复的值
        girl = []
        count += 1

file_name_boy = 'boy_' + str(count) + '.txt'                # 这一步就是把前面else的操作再执行一遍，因为文件中只有两段'======'
file_name_girl = 'girl_' + str(count) + '.txt'

boy_file = open((r"C:\Users\13326\Desktop\示例文件\%s" % file_name_boy),'w')
girl_file = open((r"C:\Users\13326\Desktop\示例文件\%s" % file_name_girl),'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()
f.close()





