#include <stdio.h>
int main(void){
double a, b, sum;
printf("Enter the first number: ");
if (scanf("%lf", &a) != 1) {
    printf("Invalid input for the first number.\n");
    return 1;
}
printf("Enter the second number: ");
if (scanf("%lf," &b) != 1) {
    printf("Invalid input for the second number.\n");
    return 1;
}
sum = a + b;
printf("Sum: %.2f\n", sum);
return 0;
}