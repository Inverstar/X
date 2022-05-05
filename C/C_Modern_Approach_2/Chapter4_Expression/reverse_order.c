#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    //成功示范，必须开辟可用的内存空间？
    char *c = (char *)malloc(sizeof(char));
    scanf("%s",c);
    printf("%s\n",c);
    return 0;
}