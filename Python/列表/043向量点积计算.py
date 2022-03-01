#在线性代数、计算几何中，向量点积是一种十分重要的运算。
#给定两个n维向量a=(a1,a2,...,an)和b=(b1,b2,...,bn)，求点积a·b=a1b1+a2b2+...+anbn。
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(n):
    a[i] *= b[i]
print(sum(a))