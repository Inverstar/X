import re
# 使用多个分隔串进行分割
a = 'long*long-ago,a beautiful0girl@chang e'
print(re.split('\*|-|,| |0|@',a))
# 为什么*之前要加\?
s = '12...34..56...a'
x = '..'
print(s.split(x))
#相邻的分隔符之间会分出空串
