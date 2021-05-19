class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]
     # 字符串 -> 从3到末尾  +  从头到3
    def __rshift__(self, other):
        return self[-other:] + self[:-other]
    # 字符串 -> 从-3到末尾   +  从头到-3

a = Nstr('I love FishC.com!')
print(a << 3)
print(a >> 3)

""" class Nstr(str):
    def __lshift__(self,other):
        temp = ''
        for i in range(other):
            temp += self[i]
        self += temp
        self = self[other:]
        return self

    def __rshift__(self,other):
        temp = ''
        for i in range(other):
            temp += self[-(i+1)]
        self = temp + self[:-other]
        return self """