from re import A


a = 12 #变量与注释
b = a
print( a + b )
'''
大小字母或下划线开头
无空格, 长度无限
预留字
赋值语句
    变量 = 表达式
'''
a, b = "he", 12
print(a,b)
a,b = b,a 
a = b = c = 10 #居然允许连续赋值
#程序顶格书写!