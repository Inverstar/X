#输入3个数求和
#2a03cc6e00fb1073214568fac5388eba83988ce7472d740b5305160930295606
a = input()
a = a.split()
b = 0
for x in a:
    b += float(x)
print(b)