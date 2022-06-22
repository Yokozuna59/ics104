##
# This program prints the user's input separate every 3 digits with a comma.
#

# Ask the user to enter number between 1,100 and 999,999
userNumber = int(input("Please enter a number between 1,100 and 999,999: "))

# Get the thousands digits using // operator
thousands = userNumber // 1000

# Get the hundreds digits using % operator
hundreds = userNumber % 1000

print("%d,%03d" %(thousands, hundreds))