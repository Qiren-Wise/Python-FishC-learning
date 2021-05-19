# 1. 写一个迭代器，要求输出至今为止的所有闰年

import datetime

class LeapYear:
    def __init__(self):
        self.leap = datetime.datetime.today().year  # 此模块可以获取到当前的年份
        self.temp = 0

    def _judge(self,year):  # 判断year是不是闰年
        if (not(year % 4) and year % 100) or not(year%400):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self._judge(self.leap):   # 如果不是闰年，年份-1，继续循环
            self.leap -= 1
        temp = self.leap  # 能出循环证明是闰年，由于我们需要迭代，我要我们先把年份赋给一个临时变量  
        self.leap -= 1  # 进行迭代
        return temp # 返回临时变量
            
               
        
test = LeapYear()
for i in test:
    if i >= 2000:
        print(i)
    else:
        break
        
# %%
