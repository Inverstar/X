#一个最简单的计算器，支持+, -, *, / 四种运算。仅需考虑输入输出为整数的情况(除法结果就是商，忽略余数）
#
s = input().split()
a , b , c = int(s[0]), int(s[1]), s[2]
if c in '+-*/':
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '*':
        print(a*b)
    else:
        if b == 0:
            print('Divided by zero!')
        else:
            print (int(a/b))
else:
    print('Invalid operator!')
