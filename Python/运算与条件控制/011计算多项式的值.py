#对于多项式f(x) = ax3 + bx2 + cx + d 和给定的a, b, c, d, x，计算f(x)的值。
#4d09b84fea0488a6ba358f229146773f4b9d78265d3ae5a3b633b25c5e8864ef
f = input().split()
x = eval(f[0])
a = eval(f[1])
b = eval(f[2])
c = eval(f[3])
d = eval(f[4])

print("%.7f"%(a*(x**3)+b*(x**2)+c*x+d))
