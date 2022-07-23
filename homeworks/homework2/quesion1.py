##
# This program implements the Taylor series expansion of the function ln(1 + x) for x in the interval (-1,1].
#

# Ask user for number of terms and checks if its in valid range
correct_answer = False
while not correct_answer:
    # Ask for number of terms
    numberOfTerm = int(input("Enter number of terms: "))

    # Check term range
    if (numberOfTerm > 0):
        correct_answer = True
    else:
        print("Error: Zero or negative number of terms not accepted")

# Ask user of   and checks if its in valid range
correct_answer = False
while not correct_answer:
    # Ask for x interval
    x = float(input("Enter the value of x in the interval (-1, 1]: "))

    # Check x interval
    if (-1 < x <= 1):
        correct_answer = True
    else:
        print("Error: Invalid value for x")

# Get the sign of x
if (x >= 0):
    signOfX = "+"
else:
    signOfX = ""

# Set result to 0
result = 0

# The result of the parameter x for the function f(x) = ln(1+x), in the interval (-1,1]
for xIndex in range(1, numberOfTerm+1):
    if (xIndex % 2 == 1):
        result += ((x**xIndex)/xIndex)
    else:
        result -= ((x**xIndex)/xIndex)

# Print result
print("The approximate value of ln(1%s%.4f) up to %d terms is %.10f" %(signOfX ,x, numberOfTerm, result))