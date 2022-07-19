##
# This program reads a positive integer and calculates number of times needed to make the integer 0 by dividing by 2.
#

# Ask the user to enter a positive integer
userInput = input("Enter a positive integer: ")

if (userInput.isdigit()):
    # Convert userInput to Integer
    userInteger = int(userInput)
    # Check if he enter 0 or not
    if (userInteger != 0):
        flag = True
    else:
        # Save result value
        result = "Not a positive integer"
        flag = False
else:
    result = "Not a positive integer"
    flag = False

# Check if it is nessesry to enter while loop
if (flag):
    # Inititlaze count as 0
    counter = 0

    # Do a while loop until userInteger equals to 0
    while userInteger > 0:
         # Floor divistion by 2
        userInteger //= 2

        # Add one to counter
        counter += 1

    # Save result value after while loop finished
    result = "We need %d integer divisions" %counter

# Prints the result
print(result)