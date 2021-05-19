# 利用递归将十进制转换为二进制(除2取余法)
def binary(x):        
    result = ''         # 先定义结果为空
    if x:
        result = binary(x//2)       # 通过不停调用binary(x//2)来不停堆栈
        return result + str(x%2)    # 将结果导入到result变量中
    else:
        return result               # 将结果返回

print(binary(89))



        

    