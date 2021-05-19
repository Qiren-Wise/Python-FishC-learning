class C2F(float):
        "摄氏度转换为华氏度"
        def __new__(cls, arg=0.0):
                return float.__new__(cls, arg * 1.8 + 32)

print(C2F(32))