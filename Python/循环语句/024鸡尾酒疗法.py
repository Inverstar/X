#鸡尾酒疗法
#5df9ac201435cd5937bb6b789fbc5fbc4ac5ac49d1f0e89a03c7addd953e4598
n = int(input()) - 1
s = input().split()
s = eval(s[1]+'/'+s[0])
while n:
    n -= 1
    x = input().split()
    x = eval(x[1]+'/'+x[0])
    if x - s > 0.05:
        print("better")
    elif s - x > 0.05:
        print("worse")
    else:
        print("same")
