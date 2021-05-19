class Stack:
        def __init__(self, start=[]):   # 初始化栈，将用户第一次传入的元素调用
                self.li = []
                for x in start:     # 循环列表中的每一项并添加
                        self.push(x)
        
        def isEmpty(self):      # 判断当前栈是否为空（返回 True 或 False）
                return not self.li

        def push(self,obj):         # 往栈的顶部压入一个数据项
                self.li.append(obj)

        def pop(self):          # 从栈顶弹出一个数据项（并在栈中删除）
                if not self.li:
                        print('警告：栈为空！')
                else:
                        return self.li.pop()

        def top(self):          # 显示当前栈顶的一个数据项
                if not self.li:
                        print('警告：栈为空！')
                else:
                        return self.li[-1]
        
        def bottom(self):       # 显示当前栈底的一个数据项
                if not self.li:
                        print('警告：栈为空！')
                else:
                        return self.li[0]

r = Stack(["a","b",'c'])
r.push('d')
print("%s" % r.bottom())


