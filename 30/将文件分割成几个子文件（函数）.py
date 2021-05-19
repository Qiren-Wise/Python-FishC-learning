def save_file(boy,girl,count):          # 这个函数执行给新文件命名、创建、写入以及关闭
        file_name_boy = 'boy_' + str(count) + '.txt'       
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open((r"C:\Users\13326\Desktop\示例文件\%s" % file_name_boy),'w')
        girl_file = open((r"C:\Users\13326\Desktop\示例文件\%s" % file_name_girl),'w')

        boy_file.writelines(boy)                
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

def split_file(file_name):          # 这个函数把文本中需要分割的字符取出来放到列表中，然后通过上面的函数完成最终的任务。                      
        count = 1
        boy = []
        girl = []

        f = open(file_name)

        for each_line in f:
                if each_line[:6] != "======":               
                        (role,line_spoken) = each_line.split('：',1)        
                        if role == '小甲鱼':
                                boy.append(line_spoken)            
                        if role == '小客服':
                                girl.append(line_spoken)
                else:
                        save_file(boy,girl,count)

                        boy = []
                        girl = []
                        count += 1
        
        save_file(boy,girl,count)
        f.close()

split_file(r"C:\Users\13326\Desktop\示例文件\record2.txt")