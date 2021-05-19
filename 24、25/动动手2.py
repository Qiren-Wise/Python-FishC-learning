def huiwen(x,start,end):
    if start > end:
        return 1
    else:
        return huiwen(x, start+1, end-1) if x[start] == x[end] else 0

string = input('请输入一串字符串：')
length = len(string)-1
if huiwen(string,0,length):
    print('"%s"是回文联' % string)
else:
    print('"%s"不是回文联' % string)