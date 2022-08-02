#include <stdio.h>

int main(void) {
    int userInput, remainder;

    printf("Enter an integer: ");
    scanf(" %d", &userInput);

    while (userInput > 0) {
        remainder = userInput % 2;
        printf("%d", remainder);

        userInput /= 2;
    }
    printf("\n");
}