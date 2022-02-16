#给定三个正整数，分别表示三条线段的长度，判断这三条线段能否构成一个三角形。
#78fd21229403d562e54cc6c3b7a79d75268124f54fc9fe46aada40eec343cb86
s = sorted(input().split())
# s = (input().split()).sort()
if eval(s[0]+'+'+s[1])>int(s[2]):
    print("yes")
else:
    print('no')
# list1 = list1.sort()