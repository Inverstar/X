#编写程序，计算下列分段函数y=f(x)的值。
#cafa7271f47cb745075353ed2d0cdf99bb5855a22711742a1eb3bf1b89afad1b
x = float(input())
if 0 <= x < 5:
    y=-x+2.5
elif 5 <= x < 10:
    y=2-1.5*(x-3)*(x-3)
else:
    y=x/2-1.5
print("%.3f"%y)