class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')
    

a = Nstr('I love FishC.com!iiiiiiii')
b = Nstr('i')

print(a - b)
