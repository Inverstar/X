s = input()
lst = s.split()
maxV = int(lst[0])
try:
    while True:
        lst = s.split()
        for x in lst:
            maxV = max(maxV,int(x))
        s = input() #ctrl+d
except:
    pass
print(maxV)