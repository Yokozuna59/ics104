##
# This program prints the prime factors of user input.
#

# Import sqrt from math
from math import sqrt

# Create function checks if number is prime or not
def isPrime(number):
    for i in range(2, int(sqrt(number))+1):
        if (number % i == 0):
            return False
    return True

# Create main function
def main():
    # Ask for input
    userInput = int(input("Enter an integer: "))
    print("Prime factors:")
    index = 2
    while userInput >= index:
        if (userInput % index == 0) and (isPrime(index)):
            print(index)
            userInput //= index
        else:
            index += 1

# Execute main
main()