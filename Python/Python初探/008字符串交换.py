#输入两个长度为4的字符串，交换这两个字符串的前两个字符后输出
#1fafc436b8c5d1195d8a5c38f082bd44b487480ac63798f125b8ac67a895df29
#字符串与列表互转
s1 = list(input())
s2 = list(input())
s1[0],s1[1],s2[0],s2[1] = s2[0],s2[1],s1[0],s1[1]
s1 = ''.join(s1)
s2 = ''.join(s2)
print(s1+'\n'+s2)