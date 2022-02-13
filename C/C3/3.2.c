#include <stdio.h>
#include <stdlib.h>
//3.2 输入圆的半径, 输出圆的周长和面积
//例1.1 已知3个整型数, 按公式s=a+b*c计算结果.
//P7
int main()
{
    int a, b, c, s;
    a = 8; b = 12; c = 6;
    s = a + b * c;
    printf("s = %d\n", s);
    return 0;
}