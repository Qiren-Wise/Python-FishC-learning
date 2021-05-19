Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str=(我爱鱼c，/n"
	 
SyntaxError: invalid character in identifier
>>> str="我爱鱼c，/n"" 正如我爱小甲鱼\n""他那呱唧呱唧的声音，\n""总缠绕于我的脑海，\n"
"久久不肯散去……\n"
	 
SyntaxError: multiple statements found while compiling a single statement
>>>  str=("我爱鱼c，/n"" 正如我爱小甲鱼\n""他那呱唧呱唧的声音，\n""总缠绕于我的脑海，\n"
"久久不肯散去……\n")
	 
SyntaxError: unexpected indent
>>> str=("我爱鱼c，/n"" 正如我爱小甲鱼\n""他那呱唧呱唧的声音，\n""总缠绕于我的脑海，\n""久久不肯散去……\n")
	 
>>> print(str)
	 
我爱鱼c，/n 正如我爱小甲鱼
他那呱唧呱唧的声音，
总缠绕于我的脑海，
久久不肯散去……

>>> str=("我爱鱼c，\n"" 正如我爱小甲鱼\n""他那呱唧呱唧的声音，\n""总缠绕于我的脑海，\n""久久不肯散去……\n")
	 
>>> print(str)
	 
我爱鱼c，
 正如我爱小甲鱼
他那呱唧呱唧的声音，
总缠绕于我的脑海，
久久不肯散去……

>>> str="""我爱鱼c，
正如1256
7895544455
64651
6161651616
1611665
"""
	 
>>> print(str)
	 
我爱鱼c，
正如1256
7895544455
64651
6161651616
1611665

>>> 
