#给定两个正整数，求它们的最大公约数。
#071242fd31b5655f52d74f599ac6efc900c175e44d26cf8e2ecb63eb5e760501
s = input().split()
print(s[0])
print(s[1])

def 最大公约数(n, m):
    if n >= m:
        if n%m == 0:
            return m
        m, n = n%m, m
        最大公约数(n,m)
    else:
        最大公约数(m,n)
print(最大公约数(int(s[0]),int(s[1])))
#返回m 后再输出结果为None?

