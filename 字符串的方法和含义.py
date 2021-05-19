#用capitalize()函数可以把第一个字符改成小写。
a1 = 'xiaoxie'
a1 = a1.capitalize()
print(a1)       
#index
#用casefold()函数可以把全部字符改成小写。
a2 = 'DAXIE'
a2 = a2.casefold()
print(a2) 

#用center(width)可以让字符串在括号标识的宽度内居中。
a3 = a2.center(40)
print(a3)

#用count(字符串[,shart[,end]])可以表示出该字符在变量中出现的次数，shart表示开始的位置，end表示结束的位置。    
a4 = a1.count('i')
print(a4)

#encoding()函数后面会讲到。

#用endswith(sub[,start[,end]])函数可以检查字符串是不是以sub字符结束，是则返回True，否则返回Flash，shart和end表示范围。
a5 = a1.endswith('xie')
print(a5)

#用expandtabs(tabsize=8)符号可以把\t转换为空格，如果不指定默认为8。
a6 = 'I\tlove\tyou'
a7 = a6.expandtabs(tabsize=10)
print(a7)

#用find(sub[,start[,end]])函数可以查找该元素在字符串内的索引值，没找到则返回-1。shart和end表示范围。
a8 = a7.find('I')
print(a8 , '在这')

#index()和find相似，不过找不到是返回一个异常。

#用isalnum()函数可以查看该字符串全部字符是不是都是字母和数字，是返回True，否返回Flash。
a9 = 'liujiajun520'
a10 = a9.isalnum()
print(a10)

#用isalphp()函数可以知道该字符串是不是全是字母，是返回True，否返回Flash。
a11 = a9.isalpha()
print(a11)

#用isdecimal()函数可以知道该字符串是不是全是十进制数字，是返回True，否返回Flash。
a12 = a9.isdecimal()
print(a12)

#用isdigit()函数可以知道该字符串是不是全是数字，是返回True，否返回Flash。
a13 = a9.isdigit()
print(a13)

#用islower()如果字符全是小写字母就返回True，否返回Flash。
a14 = 'I love China'
a15 = a14.islower()
print(a15)

#用isnumeric()可以检测字符串是不是全是数字字符，是返回True，否会显示异常。
a16 = '123456'
a17 = a16.isnumeric()
print(a17)

#用isspace()可以检测字符串是不是全是空格，是返回True，否返回Flash。
a18 = a16.isspace()
print(a18)

#用istitle()检查字符串是否标题化（所有的单词都是以大写开始，其余字母均小写），是返回True，否返回Flash。
a19 = a14.istitle()
print(a19)

#用isupper()检查字符串是不是全是大写字符，是返回True，否返回Flash。
a20 = 'ABCD'
a21 = a20.isupper()
print(a21)

#用lower()可以把全部大写字母转换成小写。
a22 = a14.lower()
print(a22)

#用lstrip()可以把字符串左边的空格全部删除。
a23 = a3.lstrip()
print(a23)

#partition(sub),可以把原字符串拆分成3元组，sub前的为一个元素，sub为一个元素，sub后的为一个元素
a24 = a20.partition('B')
print(a24)

#replace(old,new[,count])就是把旧元素替换成新元素，count就是会重复的次数。
a25 = a22.replace('china','liujiajun')
print(a25)

#rfind(sub[,start[,end]])函数和find函数类似，不过是从右边开始查找。
#rindex(sub[,start[,end]])和上面同理。

#用rjust(width)可以让字符串在width输入的宽度内右对齐，和center(width)同理。
a26 = a2.rjust(40)
print(a26)

#rpartition(sub)和partition差不多，不过是从右边开始查找。
#rstrip和lstrip()同理，这是删除字符串末尾的空格。

#split(sep=None,  maxsplit=-1),以sep设定的元素来划分一个列表，如果不设置，默认以空格来划分列表。如果后面的值也有设置则只划分该个数的列表元素。
a27 = a25.split('u')
print(a27)

#splitlines(([keepends]))是按'\n'分隔，返回一个列表，如果keepends有指定，则返回前keepends行。

#startswith(prefix[,start[,end]])查看字符串是不是以prefix所选的元素开头，是返回True，否返回Flash。
a28 = a25.startswith('i')
print(a28)

#strip([chars])删除字符串左右两边的空格，或者可以用chars来指定要删除的参数。

#swapcase()可以翻转字符串全部的大小写。
a29 = a14.swapcase()
print(a29)

#title()可以让字符串标题化，所有的单词都是以大写开始，其余字母均小写。
a30 = a25.title()
print(a30)

#translate(table)根据table的规则（可以由str.maketrans(‘a’,‘b’)定制）转换字符串中的字符。
a31 = a22.translate(str.maketrans('i','L'))
print(a31)

#upper()和lower类似，可以把小写字符转换成大写。

#zfill(width)可以让字符串右对齐，然后前面用0填充。
a32 = a2.zfill(40)
print(a32)