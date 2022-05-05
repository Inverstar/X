#include <stdio.h>
// 测试各种类型与运算符
int main(void)
{
    // %取余只对整数起作用 负数取余结果为负
    // C99中除法结果趋0取整
    int c = 0;
    int t = 1;
    float f = 11.3f;
    printf("%f,%f\n",f/t,t/f);
    printf("%d %d",-9/7,-9%3);
    return 0;
}