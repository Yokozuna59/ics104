#include <stdio.h>

int main(void) {
    int sum, userInput;
    sum = 0;
    userInput = 0;

    while (userInput >= 0) {
        printf("Enter a positive number (or a negative value to finish): ");
        scanf(" %d", &userInput);

        if (userInput >= 0)
            sum += userInput;
    }

    if (sum != 0)
        printf("Sum = %d\n", sum);
    else
        printf("No positive number was entered.\n");
}