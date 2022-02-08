//#include <stdafx.h>
#include <stdio.h>
#include <stdlib.h>
//2.2.2 变量与变量定义
//例2.2 字符型变量定义及赋初值
//P21
void main()
{
    char c1, c2;
    c1 = 'a'; c2 = 'b';
    c1 = c1-32; c2 = c2 -32;
    //'A'的ASCII码是65, 97是'a'.
    printf("%c %c\n", c1, c2);
    //return 0;
}