##
# This program reads two integers (a, b) and finds their GCD (greatest common divisor).
#

# Ask the user to enter the to integer
a = int(input("Enter the first positive integer: "))
b = int(input("Enter the second positive integer: "))

# Get the least integer of a and b which is the GCD so far
greatestCommonDivisor = min(a, b)

# Set flag to True
flag = True

# while loop until flag becomes False
while flag:
    # Get the remainder of a and b by mod number
    aModulo = a % greatestCommonDivisor
    bModulo = b % greatestCommonDivisor

    # Check if the mod values of a and b is 0
    if (aModulo == 0) and (bModulo == 0):
        # Print the result
        print("THe GCD of %d and %d is %d" %(a, b, greatestCommonDivisor))

        # Set flag to Flase
        flag = False
    # Subtract one to
    greatestCommonDivisor -= 1

##########################################################################

# Or a shorter way to do the same thing

# Import greatest common divisor function from math module
from math import gcd

# Get the GCD of a and b
greatestCommonDivisor = gcd(a, b)

# Print the result
print("THe GCD of %d and %d is %d" %(a, b, greatestCommonDivisor))