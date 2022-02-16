#利用公式x1 = (-b + sqrt(b*b-4*a*c))/(2*a), x2 = (-b - sqrt(b*b-4*a*c))/(2*a)求一元二次方程ax2+ bx + c =0的根，其中a不等于0。
#cb07dc6e5e4869ed0704a2a2b03d282944b0e10cb2ee907cb3c5c74752d8e4af
import math
s = input().split()
a = float(s[0])
b = float(s[1])
c = float(s[2])
b2 = 4*a*c

if b**2 == b2:
    print('x1=x2=%.5f'%((math.sqrt(b * b - b2) -b) / (2 * a) ))
elif b**2 > b2:
    print('x1=%.5f;x2=%.5f'%((math.sqrt(b * b - b2) -b) / (2 * a) ,
    (-b-math.sqrt(b*b-b2))/(2 * a)))
else:
    x = b/(-2*a)
    if x == 0:
        x = 0
    i = math.sqrt(b2-b*b)/(2*a)
    print('x1=%.5f+%.5fi'%(x,i),end=';')
    print('x2=%.5f-%.5fi'%(x,i))