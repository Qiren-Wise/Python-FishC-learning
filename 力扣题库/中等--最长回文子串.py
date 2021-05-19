import time
starttime = time.time()

s = input('找出字符串中的最长回文字符\n请输入：')
def search(s):
    length = len(s)
    new = []
    for each_one in range(length):
        for each_two in range(length,-1,-1):
            start = s[each_one:each_two]
            end = s[each_two-1:each_one:-1] + s[each_one]
            if start == end:
                new.append(start)
                break
    return new

new = search(s)
max = new[0]
for each in new:
    length = len(each)
    if length > len(max):
        max = each
print('该字符串的最大回文字符串是：%s' % max)

endtime = time.time()      
print('本次程序执行时间：%s 秒' % round(endtime - starttime,3))
