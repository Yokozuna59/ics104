##
# This program reads an integer from the user and prints the sum of the digits.
#

# Initialize the count, sum and flag variables
count = 0
theSum = 0
flag = True

while flag:
    # Ask user to enter a positive integer value
    userInput = input("Enter a positive number (or a negative value to finish): ")

    # Check if the user entered a empty string
    if (userInput != ""):
        # Convert to integer
        intUserInput = int(userInput)

        if (intUserInput >= 0):
            # Add 1 to the count
            count += 1

            # Add the integer to the sum
            theSum += intUserInput
        else:
            # Set flag to false
            flag = False

# Print the result
if (theSum != 0):
    print("Sum = %.1f" %theSum)
else:
    print("No positive number was entered.")