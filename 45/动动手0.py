import time as t

# 自己的方法，利用时间戳来计算(下面还有小甲鱼的方法)
class MyTimer:
    def __init__(self): #用于初始化变量
        self.prompt = '未开始计时'
        self.begin = 0  #开始时间
        self.end = 0  #结束时间
        #self.unit = ['年','月','天','时','分','秒']
    
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    def __add__(self,other):
        prompt = '总共计时'
        result = self.intervel + other.intervel
        prompt += str(result)
        return round(prompt,3)

    def start(self):    #开始计时
        self.begin = t.time()
        print('开始计时')
        

    def stop(self):     #结束计时
        if not self.begin:
            print('请先开始计时！')
        else:
            self.end = t.time()
            self._calc()
            print('结束计时')
        

    def _calc(self):    #内部方法，用于计算开始到结束相差的时间
        self.intervel = 0
        self.prompt = '本次计时'

        self.intervel = self.end - self.begin

        if self.intervel < 1:   #毫秒
                self.intervel = str(round(self.intervel*1000,3)) + ' ms'
        elif self.intervel < 60:    #秒
                self.prompt += str(round(self.intervel,3)) + ' s'
        elif self.intervel < 3600:      #分钟
                self.prompt += str(self.intervel // 60) + ' min ' + str(round(self.intervel % 60,3)) + ' s'
        else:    #小时
                self.prompt += str(self.intervel //60//60) + ' h ' + str(self.intervel //60%60) + 'min'

        self.begin = 0
        self.end = 0

t1 = MyTimer()
t2 = MyTimer()
t1.start()
t.sleep(2)
t1.stop()
t2.start()
t.sleep(2)
t2.stop()
print(t1)
print(t2)
print(t1+t2)


# 这是小甲鱼的方法(利用向高位借位的方法)
class FcMyTimer:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.borrow = [0, 12, 31, 24, 60, 60]
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0
        self.end = 0
    
    def __str__(self):
        return self.prompt
 
    __repr__ = __str__
 
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    
    # 开始计时
    def start(self):
        # self.begin = t.localtime()
        self.begin = [2022,2,22,16,30,30]
        self.prompt = "提示：请先调用 stop() 停止计时！"
        print("计时开始...")
        # [2022,2,22,16,30,30]
    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用 start() 进行计时！")
        else:
            #self.end = t.localtime()
            self.end = [2025,2,22,15,30,30]
            self._calc()
            print("计时结束！")
        # [2025,2,22,15,30,30]
 
    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            temp = self.end[index] - self.begin[index]
 
            # 低位不够减，需向高位借位 
            if temp < 0:
                # 测试高位是否有得“借”，没得借的话向再高位借......
                i = 1
                while self.lasted[index-i] < 1:
                    self.lasted[index-i] += self.borrow[index-i] - 1
                    self.lasted[index-i-1] -= 1
                    i += 1
                #self.borrow = [0, 12, 31, 24, 60, 60]
                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index-1] -= 1
            else:
                self.lasted.append(temp)
 
        # 由于高位随时会被借位，所以打印要放在最后
        for index in range(6):
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
        
        # 为下一轮计时初始化变量
        self.begin = 0
        self.end = 0


a = FcMyTimer()
b = FcMyTimer()
a.start()
a.stop()
print(a)


