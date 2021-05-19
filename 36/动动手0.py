from easygui import *
import random

secret = random.randint(1,10)
title = '小游戏'
print(secret)
if ynbox(title='我爱鱼C工作室',msg='是否开始游戏',choices=['开始','结束']):
    for each in range(3):
        num = integerbox('不妨猜一下小甲鱼现在心里想的是哪个数字：',title,lowerbound = 1,upperbound = 10)
        if each != 2:
            if num > secret:
                if ynbox('哥，大了大了',title,choices=['继续游戏','结束游戏']) == False:
                    break
            elif num < secret:
                if ynbox('哥，小了小了',title,choices=['继续游戏','结束游戏']) == False:
                    break
            else:
                msgbox('我草，你是小甲鱼心里的蛔虫吗？！\n哼，猜中了也没有奖励！',title,'结束游戏')
                break
    else:
        msgbox(msg = '机会用光咯~',title = title)

msgbox('游戏结束，不玩啦',title,ok_button='好的')
        