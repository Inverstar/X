//#include <stdafx.h>
#include <stdio.h>
#include <stdlib.h>
//2.2.2 变量与变量定义
//例2.1 整型变量定义及赋初值
//P21
void main()
{
    int x, y, z, w;
    unsigned int k;
    float c = 1.1;
    int i = 10;
    
    x = 10; y = -20; k = 30;
    z = x + k; w = y + k;
    printf("%f\n", i + c);
    printf("x + y = %d\ny + d = %d\n", z, w);
    //return 0;
}