
def phone(program,name):
   
    # 打印题目所要求的第一段
    print('|--- 欢迎进入通讯录程序 ---|')
    for i in program:
        print('|--- ',i,':',program[i],' ---|')

    while True:
        x = int(input('\n请输入相关的指令代码：'))

        if x == 1:
            y = input('请输入联系人姓名：')
            if y in name:
                print(y,':',name[y])
            else:
                print('查找不到该联系人！')
            
        elif x == 2:
            y = input('请输入新联系人姓名：')
            if y in name:
                print('您输入的姓名在通讯录中已存在 -->> ', y ,':', name[y])
                yn = input('是否修改用户资料(YES/NO):')
                if yn == 'YES':
                    name[y] = input('请输入用户联系电话：')
            else:
                name[y] = input('请输入用户联系电话：')

        elif x == 3:
            y = input('请输入需要删除的联系人：')
            if y in name:
                name.pop(y)
            else:
                print('本通讯录中没有该联系人！')
        else:
            print('|--- 感谢使用通讯录程序 ---|')
            break

program = {1:'查询联系人资料',2:'插入新的联系人',3:'删除已有联系人',4:'退出通讯录程序'}
name = {'小甲鱼':'020-88888888','刘佳俊':'199****4694','李起龙':'183****8557'}
phone(program,name)


