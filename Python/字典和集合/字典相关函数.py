d = {1:89,2:11}
i = 89
if i in d:
    print(i,d)
for i in d.keys():
    print(i)
print(d.keys())
for i in d.values():
    print(i)
print(d.values)
for i in d.items():
    print(i)
for i,j in d.items():
    print(i,j)
#元素序列, 用于遍历
a = d.copy()

d.pop(1)
#删除键为1的元素, 不存在则产生异常

d.clear()
print(d)