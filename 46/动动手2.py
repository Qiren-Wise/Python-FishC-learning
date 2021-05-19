class Counter:
        def __init__(self):
                super().__setattr__('counter', 0)   # 在基类中定义一个counter属性为0

        def __setattr__(self, name, value):
                super().__setattr__('counter', self.counter + 1)    # 给counter属性重新赋值，赋值的值为原数值+1
                super().__setattr__(name, value)

        def __delattr__(self, name):
                super().__setattr__('counter', self.counter - 1)
                super().__delattr__(name)

