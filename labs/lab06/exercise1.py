##
# This program reads user input asking for an integer, then prints the binary integer reversed order.
#

# Ask user to enter a positive integer value
userInputInteger = int(input("Enter an integer: "))

# Print the binary integer reversed order
print("The binary digits in reverse order are", end=" ")

# While loop until userInputInteger is greater than 0
while userInputInteger > 0:
    # Get the remainder of userInputInteger Modulo 2
    remainder = userInputInteger % 2

    # Print the remainder of the integer
    print(remainder, end="")

    # Floor divide the integer by 2
    userInputInteger //= 2
print()