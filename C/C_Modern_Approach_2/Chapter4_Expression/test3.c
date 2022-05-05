#include <stdio.h>
// 测试各种类型与运算符
// 明天继续，还是很有意思的啊
int main(void)
{
    int i = 0;
    int a[] = {1,2,3};
    a[i++] = a[i++]+2;
    //先让a[0]+2，之后i+1，改变的是a[1]的值为3
    //表达式完成后i+1
    //这时的i自增几次？何时自增？
    printf("%d,%d,%d\n",a[0],a[1],a[2]);
    printf("%d,%d\n",a[i],i);
    return 0;
}