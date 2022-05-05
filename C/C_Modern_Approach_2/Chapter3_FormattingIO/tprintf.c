// 格式化输出数字
#include <stdio.h>
int main(void)
{
    int i;
    float x;
    printf("%d,%f,%d\n\a",i,x);
    i = 40;
    x = -893.21f;
    printf("|%d|%5d|%-5d|%5.3d|\n",i,i,i,i);
    printf("|%10.3f|%10.3e|%--10g|\n",x,x,x);
    return 0;
}