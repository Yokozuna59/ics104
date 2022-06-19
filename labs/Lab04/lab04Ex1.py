##
# This program read three integers and checks if they are in order or not.
#

# Ask user to enter 3 integers
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
thirdNumber = int(input("Enter third number: "))

# Create a variable for integers in one string
userNumbers = "%d %d %d" %(firstNumber, secondNumber, thirdNumber)

# Check if numbers are asending order
if (firstNumber >= secondNumber >= thirdNumber):
    order = "in order"
# Check if numbers are in desending order
elif (firstNumber <= secondNumber <= thirdNumber):
    order = "in order"
else:
    order = "not in order"

# Print the result
print(userNumbers, order)