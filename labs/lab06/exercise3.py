##
# This program reads an integer from the user and prints the number of digits the sum of them.
#

# Ask user to enter a positive integer value
userPositiveInteger = input("Enter a positive integer value: ")

# Get the length of the user input
length=len(userPositiveInteger)

# Initialize the sum variable
sumOfIntegers = 0

for integer in userPositiveInteger:
    # Convert to integer
    convertToInteger = int(integer)

    # Add to sum
    sumOfIntegers += convertToInteger

# Print the result
print("Your integer has %d digits and their sum is %s" %(length, sumOfIntegers))