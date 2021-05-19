import easygui as g
 
msg = "请填写以下联系方式"
title = "账号中心"
fieldNames = [" *用户名", " *真实姓名", "  固定电话", " *手机号码", "  QQ", " *E-mail"]
fieldValues = []
fieldValues = g.multenterbox(msg,title, fieldNames)    # 先把第一次输入的结果赋值给fieldValues
 
while 1:
    if fieldValues == None:
        break   # 如果点击取消按钮，就会返回None，那么说明想手动结束程序了，即跳出循环
    errmsg = ""
    for i in range(len(fieldNames)):    # 以fieldNames的长度定义一个循环
        option = fieldNames[i].strip()  # 删除fieldNames两边的空白字符
        if fieldValues[i].strip() == "" and option[0] == "*":   # 如果fieldValues的第i项取出空格后是''，并且这一项还是必输入项
            errmsg += ('【%s】为必填项。\n\n' % fieldNames[i])    # 就添加上需要警告的字符
    if errmsg == "":    # 如果没有需要警告的字符，就跳出循环
        break
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)    # 当有需要警告的字符时，再次调用输入框
 
print("用户资料如下：%s" % str(fieldValues))
    

'''
# 自己编写的
from easygui import *
write = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
msg = '请登记用户信息'

while True:
    content = multenterbox(msg,'账号中心',fields = write)
    count = 0
    msg = ''
    if content == None:
        msgbox('游戏结束')
        break
    for each in content:
        count += 1
        if each == '' or each.isspace():
            if count == 3 or count == 5:
                continue
            else:
                msg += '【%s】为必填项\n' % write[count-1]
                         
    if content[0] != '' and content[1] != '' and content[3] != '' and content[5] != '' \
            and content[0].isspace() == False and content[1].isspace() == False and content[3].isspace() == False and content[5].isspace() == False:
            break

new_msg = '用户资料如下：\n\n'
one = 0
if content != None:
    for i in write:
        new_msg += i + '： ' + content[one] + '\n\n'
        one += 1
    msgbox(new_msg,'账户中心')
'''
    
        
             
    
                


