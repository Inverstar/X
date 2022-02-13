#列表[]
list1 = [1,2,3]
print(list1[0])
for x in list1:
    print(x)
list1[2] = 0
a = 1
list1[a]

#利用字符串分隔处理一行的数据
s = input()
numbers = s.split()
print(int(numbers[0])+int(numbers[1]))

#split() 空格,制表符,换行符分隔得到的列表
