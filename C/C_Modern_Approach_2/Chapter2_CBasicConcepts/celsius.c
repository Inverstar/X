// Converts a Fahrenheit temperature to Celsius
#include <stdio.h>
#define FREEZING_PI 32.0f
#define SCALE_FACTOR (5.0f/9.0f)
int celsius(void)
{
    float fahrenheit = 0, celsius = 0;
    printf("Enter Fahrenheit temperature: ");
    scanf_s("%f",&fahrenheit);
    celsius = (fahrenheit - FREEZING_PI) * SCALE_FACTOR;
    printf("Celsius equivalent: %1f\n", celsius);
    return 0;
    // exit(0);
}