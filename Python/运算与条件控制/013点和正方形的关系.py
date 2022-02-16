"""
有一个正方形，四个角的坐标（x,y)
分别是（1，-1），（1，1），（-1，-1），（-1，1），
x是横轴，y是纵轴。写一个程序，判断一个给定的点是否在这个正方形内（包括正方形边界）。
"""
#834663c2d597f27d7ddefcb950838344004e1b2fecf49e7c81ed437a05d7b422
zuobiao = input().split()
if -1<=int(zuobiao[0])<=1:
    if -1<=int(zuobiao[1])<=1:   
        print('yes')
    else:
     print('no')
else:
     print('no')
