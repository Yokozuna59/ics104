#include <stdio.h>

int main(void) {
    int number, thousnd, hunderd;
    printf("Please enter a number between 1,100 and 999,999: ");
    scanf("%d", &number);

    thousnd = number/1000;
    printf("%d,", thousnd);
    hunderd = number % 1000;
    printf("%03d\n", hunderd);
}