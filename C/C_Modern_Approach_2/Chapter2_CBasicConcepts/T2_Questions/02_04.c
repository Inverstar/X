#include <stdio.h>
int T0204(void){
    float amount;
    printf("Enter an amount: ");
    scanf("%f",&amount);
    printf("With tax added: $%.2f",amount*1.05);
   return 0;
}
