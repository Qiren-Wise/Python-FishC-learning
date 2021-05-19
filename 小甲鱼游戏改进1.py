import random
secret = random.randint(1,10)
print("------------我爱鱼c工作室-----------")
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
i=1
if guess == secret:
        print("卧槽，你是小甲鱼心里的蛆虫吗？！")
        print("哼，猜中了也没有奖励!")
else:
        if guess > secret:
            print("哥，大了，大了")
        else:
            print("哥，小了，小了")
while guess != secret and i <= 2:
    temp = input("哎呀，猜错了，请重新输入：")
    guess = int(temp)
    if guess ==secret:
        print("卧槽，你是小甲鱼心里的蛆虫吗？！")
        print("哼，猜中了也没有奖励!")
    else:
        if guess > secret:
            print("哥，大了，大了")
            i=i+1
        else:
            print("哥，小了，小了")
            i=i+1
print("游戏结束，不玩啦！")

    
