class Nint(int):
        def __new__(cls,num):
                if isinstance(num,str):
                        sum = 0
                        for i in num:
                                sum += ord(i)
                        num = sum
                return int.__new__(cls,num)



print(Nint('FishC'))                  
                       