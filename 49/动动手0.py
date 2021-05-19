# 0. 用 while 语句实现与以下 for 语句相同的功能：
# for each in range(5):
#     print(each)

n = range(5)
it = iter(n)
while 1:
        try:
                print(next(it))
        except StopIteration:
                break


# 更麻烦的一种方法....
'''
class Demo:
    def __init__(self,n = 5):
        self.a = -1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.a += 1
        if self.a < self.n:
            return self.a
        else:
            raise StopIteration

test = Demo()
iter(test)
while 1:
    try:
        print(next(test))
    except StopIteration:
        break
'''