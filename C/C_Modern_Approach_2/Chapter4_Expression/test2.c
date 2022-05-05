#include <stdio.h>
// 连续赋值运算
int main(void)
{
    // 前一个赋值语句的值
    // 赋值对象必须是左值
    // i *= c + f 即 i = i*(c+f)
    int c = 0,k;
    int t = 2;
    float f = 11.3f;
    f = c = 33.2f;
    f += c += 1;
    t *= f + c;
    printf("%d\n",t);
    f = 1.0f;
    t = k = 5;
    // c = (k=t+2)-(t=1);
    c = -(t=1)+(k=t+2);
    // c = t*t++;
    printf("%d\n",c);
    return 0;
}