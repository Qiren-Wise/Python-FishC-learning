class Demo:
    def __getattr__(self,name):
        self.name = 'FishC'
        return self.name

d = Demo()
print(d.x)
d.x = 'X-man'
print(d.x)