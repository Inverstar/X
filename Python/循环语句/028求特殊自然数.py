#一个十进制自然数,它的七进制与九进制表示都是三位数，且七进制与九进制的三位数码表示顺序正好相反。编程求此自然数,并输出显示。
#6d87879b5bcbe92fac27f9986b4be4bdf349438f202c39ff899e07ffc16d3007
for x in range(81,553):
    if x%7 == x//81:
        x1 = str(x%7)
        if x//7%7 == x//9%9:
            x2 = str(x//7%7)
            if x//49 == x%9:
                x3 = str(x//49)
                print(x)
                print(x3+x2+x1)
                print(x1+x2+x3)
                break
    