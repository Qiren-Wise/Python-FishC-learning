class FileObject:
    def __init__(self,fileName):
        self.f = open("%s" % fileName,'w',encoding='utf-8')

    def content(self):
        self.message = input("请输入内容：")
        self.f.write(self.message)

    def __del__(self):
        self.f.close()
        del self.f

def begin():
    fileWay = input("请输入路径名：")
    a = FileObject(fileWay)
    a.content()

begin()