# 你买了一箱n个苹果，很不幸的是买完时箱子里混进了一条虫子。虫子每x小时能吃掉一个苹果，假设虫子在吃完一个苹果之前不会吃另一个，那么经过y小时你还有多少个完整的苹果？
#63514eac02e381f0a6ee732f045e46f7391b1a71650782cf8cf04f197ce1a48c
s = input().split()
n = int(s[0])
x = int(s[1])
y = int(s[2])
if y == 0:
    print(n)
elif n>0:
    if y<x:
        print(n-1)
    else:
        if y%x == 0:
            if n-y/x < 0:
                print(0)
            else:
                print(n-y//x)
        else:
            if n - y//x - 1<0:
                print(0)
            else:
                print(n-y//x-1)
else:
    print(0)