#include <stdio.h>
#include <math.h>

int isPrime(int n) {
    for (int i = 2; i < (int)sqrt(n)+1; i++) {
        if (n%i == 0)
            return 0;
    }
    return 1;
}

int main(void) {
    for (int i = 2; i < 100; i++) {
        if (isPrime(i))
            printf("%d\n", i);
    }
}