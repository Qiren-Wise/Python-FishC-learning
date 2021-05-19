import random           #引入一个随机函数

times = 3               #可用次数为3
secret = random.randint(1,10)           #随机数范围

print('------------------我爱鱼C工作室------------------')
guess = 0
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")

while (guess != secret) and (times > 0):                 #条件为真时执行的效果
        temp = input()          #赋值

        if temp.isdigit():
                guess = int(temp)
                if guess == secret:
                        print("我草，你是小甲鱼心里的蛔虫吗？！")
                        print("哼，猜中了也没有奖励！")
                else:
                        if guess > secret:
                                print("哥，大了，大了")
                        else:
                                print("哥，小了，小了")
                        if times > 1:
                                print("再试一次吧：", end=' ')
                        else:
                                print('机会用光咯')
        else:
                print('抱歉，你的输入有误，请重新输入：', end=' ')
        times = times - 1                 # 用户每输入一次，可用机会就-1
print('游戏结束，不玩啦')
                
                        
