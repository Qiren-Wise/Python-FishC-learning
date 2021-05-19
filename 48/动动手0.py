'''
0. 根据课堂上的例子，定制一个列表，同样要求记录列表中每个元素被访问的次数。
这一次我们希望定制的列表功能更加全面一些，比如支持 append()、pop()、extend() 原生列表所拥有的方法。你应该如何修改呢？
要求1：实现获取、设置和删除一个元素的行为（删除一个元素的时候对应的计数器也会被删除）
要求2：增加 counter(index) 方法，返回 index 参数所指定的元素记录的访问次数
要求3：实现 append()、pop()、remove()、insert()、clear() 和 reverse() 方法（重写这些方法的时候注意考虑计数器的对应改变）
'''

# 小甲鱼的方法，借用了列表的继承属性
class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)
 
    def __len__(self):
        return len(self.count)
 
    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)
 
    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)
 
    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)
 
    def counter(self, key):
        return self.count[key]
 
    def append(self, value):
        self.count.append(0)
        super().append(value)
 
    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)
 
    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)
 
    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)
 
    def clear(self):
        self.count.clear()
        super().clear()
 
    def reverse(self):
        self.count.reverse()
        super().reverse()


# 我的笨方法，呜呜呜~舍不得删
class Immobile:
    def __init__(self,*value):
        self.li = [x for x in value]
        self.count = {}.fromkeys(range(len(self.li)),0)
    
    def __len__(self):
        return len(self.li)

    def __getitem__(self,key):
        self.count[key] += 1
        return self.li[key]

    def __setitem__(self,key,value):
        self.li[key] = value

    def append(self,value):
        self.li.append(value)
        self.count[len(self.li)-1] = 0

    def pop(self):
        self.li.pop()
        self.count.popitem()

    def remove(self,key):
        self.count.pop(self.li.index(key))
        self.li.remove(key)
        for i in range(len(self.li)):
            if  self.count.get(i) == None:
                self.count[i] = self.count[i+1]
                self.count.pop(i+1)

    def insert(self,key,value):
        self.li.insert(key,value)
        self.count[7] = 0
        for i in range(len(self.li)-1,key-1,-1):
            if i != key:
                self.count[i] = self.count[i-1]
            else:
                self.count[i] = 0

    def clear(self):
        self.li.clear()
        self.count.clear()

    def reverse(self):
        self.li.reverse()
        left = 0
        right = len(self.li)-1
        while left < right:
            tmp = self.count[left]
            self.count[left] = self.count[right]
            self.count[right] = tmp
            left += 1
            right -= 1

    def counter(self,key):
        return self.count[key]

