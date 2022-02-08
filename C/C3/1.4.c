//#include <stdafx.h>
#include <stdio.h>
#include <stdlib.h>
//1.4 C语言程序的基本结构
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