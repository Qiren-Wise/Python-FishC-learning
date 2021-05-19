#1. 你可以利用异常的原理，修改下面的代码使得更高效率的实现吗？
'''
print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')
 
contacts = dict()
 
while 1:
    instr = int(input('\n请输入相关的指令代码：'))
    
    if instr == 1:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print(name + ' : ' + contacts[name])
        else:
            print('您输入的姓名不再通讯录中！')
 
    if instr == 2:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + ' : ' + contacts[name])
            if input('是否修改用户资料（YES/NO）：') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        else:
            contacts[name] = input('请输入用户联系电话：')
 
    if instr == 3:
        name = input('请输入联系人姓名：')
        if name in contacts:
            del(contacts[name])         # 也可以使用dict.pop()
        else:
            print('您输入的联系人不存在。')
            
    if instr == 4:
        break
 
print('|--- 感谢使用通讯录程序 ---|')
'''


#答案
print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')
 
contacts = dict()
 
while 1:
    try:
        instr = int(input('\n请输入相关的指令代码：'))
    except ValueError as reason:
        print('只能输入指定程序命令噢~')
    else:
        if instr > 4 or instr < 0:
            print('只能输入指定程序命令噢~')
            
        if instr == 1:
            name = input('请输入联系人姓名：')
            try:
                print(name + ' : ' + contacts[name])
            except:
                print('您输入的姓名不再通讯录中！')
    
        if instr == 2:
            name = input('请输入联系人姓名：')
            try:
                contacts[name]
                print('您输入的姓名在通讯录中已存在 -->> ', end='')
                print(name + ' : ' + contacts[name])
                if input('是否修改用户资料（YES/NO）：') == 'YES':
                    contacts[name] = input('请输入用户联系电话：')
            except:
                contacts[name] = input('请输入用户联系电话：')
    
        if instr == 3:
            name = input('请输入联系人姓名：')
            try:
                del(contacts[name])         # 也可以使用dict.pop()
            except:
                print('您输入的联系人不存在。')
                
        if instr == 4:
            break

print('|--- 感谢使用通讯录程序 ---|')