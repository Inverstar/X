#给定一个长度为n的非负整数序列，请计算序列的最大跨度值（最大跨度值 = 最大值减去最小值）。
#b7f6cac73d047706327ad06b8bd97dd34a6f71b8c114927449cc222f5e0bd243
n = input()
s = input().split()
maxV = minV = int(s[0])
for x in s:
    if maxV < int(x):
        maxV = int(x)
    minV = min(minV,int(x))
print(maxV-minV)