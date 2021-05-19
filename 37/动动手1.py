class Rectangle():
    width = 5
    length = 10
    def setRect(self):
        print('请输入矩形的长和宽...')
        self.length = int(input("长："))
        self.width = int(input('宽：'))
    
    def getRect(self):
        print('这个矩形的长是：%d，宽是：%d' % (self.length,self.width))
    
    def getArea(self):
        return self.length * self.width
        #area = self.length * self.width
        #print('这个矩形的面积是：%d' % area)

a = Rectangle()
print(a.getArea())