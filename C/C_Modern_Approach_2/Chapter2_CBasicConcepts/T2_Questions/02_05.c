#include <stdio.h>
int T0205(void)
{
    float x;
    printf("Enter an value of X: ");
    scanf_s("%f",&x);
    float result = 3*x*x*x*x*x + 2*x*x*x*x - 5*x*x*x -x*x + 7*x - 6;
    printf("The Result of the polynomial: %f\n",result);
   return 0;
}
