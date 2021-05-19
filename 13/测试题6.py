list1 = ['1.Jost do It','2.一切皆有可能','3.让编程改变世界','4.Imossible']
list2 = ['4.阿迪达斯','3.李宁','2.鱼C工作室','1.耐克']
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
for each in list3:
    print(each)

