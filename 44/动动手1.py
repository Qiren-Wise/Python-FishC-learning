class Word(str):
    def __new__(cls,words):
        if ' ' in words:
            print("存在空格，仅保留空格前的值")
            words = words.split(' ',1)[0]   
        return str.__new__(cls,words)

    def __gt__(self,other): # 大于
        return len(self) > len(other)
    
    def __ge__(self,other): # 大于等于
        return len(self) >= len(other)

    def __le__(self,other): # 小于等于
        return len(self) <= len(other)

    def __lt__(self,other): # 小于
        return len(self) < len(other)

a = Word('abcdea')
b = Word('abcde   aadaff')
print(a>b)


class NewWord(str):
    '''存储单词的类，定义比较单词的几种方法'''
 
    def __new__(cls, word):
        # 注意我们必须要用到 __new__ 方法，因为 str 是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
        return str.__new__(cls, word)
 
    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

        