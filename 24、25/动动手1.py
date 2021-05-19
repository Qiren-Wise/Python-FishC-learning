result = []             # 先定义一个空字符串          
def get_digits(n):
    if n:
        result.insert(0,n%10)       # 把n%10的结果输入到result这个列表中
        get_digits(n//10)           # n//10同时再次调用这个函数
    return result                   # 返回结果到列表result

print(get_digits(12345))