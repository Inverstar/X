#2008年北京奥运会，A国的运动员参与了n天的决赛项目(1≤n≤17)。现在要统计一下A国所获得的金、银、铜牌数目及总奖牌数。
#030049e5f2e638b55e285fbbca4c4b5610b2a885538bb6b96ee070cf36ad9447
n = int(input())
j = y = t = z = 0
while n:
    n -= 1
    s = input().split()
    j += int(s[0])
    y += int(s[1])
    t += int(s[2])
z = j+y+t
print(j,y,t,z)
