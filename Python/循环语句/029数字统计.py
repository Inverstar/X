#请统计某个给定范围[L, R]的所有整数中，数字2出现的次数。
#比如给定范围[2, 22]，数字2在数2中出现了1次，在数12中出现1次，在数20中出现1次，在数21中出现1次，在数22中出现2次，所以数字2在该范围内一共出现了6次。
#2dbf6ee615c706dc7f765f729569924a6a0906e048d3116d34619e010247f11f
s = input().split()
L,R = int(s[0]),int(s[1])
total = 0
for i in range(L,R+1):
    # s = str(i)
    # for x in s:
    #     if x == '2':
    #         total +=1
    while i != 0:
        m = i % 10
        if m == 2:
            total += 1
        i //= 10
print(total)

