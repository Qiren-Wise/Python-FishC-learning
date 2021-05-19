file_name = input('请输入文件名：')
old_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
def Replace(file_name,old_word,new_word):
    f = open(file_name)
    count = 0
    content = []

    for each in f:
        if old_word in each:
            count += each.count(old_word)
            each = each.replace(old_word,new_word)
        content.append(each)
    
    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
                   % (file_name, count, old_word, old_word, new_word))
    
    if decide in ['YES','Yes','yes']:
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()

    f.close()

Replace(file_name,old_word,new_word)
