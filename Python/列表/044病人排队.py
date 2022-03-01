#病人登记看病，编写一个程序，将登记的病人按照以下原则排出看病的先后顺序： 
#1. 老年人（年龄 >= 60岁）比非老年人优先看病。 
#2. 老年人按年龄从大到小的顺序看病，年龄相同的按登记的先后顺序排序。 
#3. 非老年人按登记的先后顺序看病。
n = int(input())
a = []
def s(x):
    if x[1] >= '60':
        return (-1,-int(x[1]))
    else:
        return (1,0)
for i in range(n):
    a.append(tuple(input().split()))
a.sort(key = s)
for i in range(n):
    print(a[i][0])