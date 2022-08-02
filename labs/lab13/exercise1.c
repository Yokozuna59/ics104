#include <stdio.h>

int main(void) {
    int firstNumber, secondNumber, thirdNumber;

    printf("Enter the first number: ");
    scanf(" %d", &firstNumber);

    printf("Enter the second number: ");
    scanf(" %d", &secondNumber);

    printf("Enter the third number: ");
    scanf(" %d", &thirdNumber);

    if (firstNumber <= secondNumber && secondNumber <= thirdNumber)
        printf("%d %d %d in order\n", firstNumber, secondNumber, thirdNumber);
    else if (firstNumber >= secondNumber && secondNumber >= thirdNumber)
        printf("%d %d %d in order\n", firstNumber, secondNumber, thirdNumber);
    else
        printf("%d %d %d not in order\n", firstNumber, secondNumber, thirdNumber);
}