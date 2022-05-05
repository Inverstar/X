#include <stdio.h>
int main(void)
{
    // 12.3 45.6 789
    float i,j;
    int x;
    scanf("%f%d%f",&i,&x,&j);
    printf("%f %d %f\n",i,x,j);
    printf("%d %f %d",i,x,j);
    printf("\n");
    return 0;

}