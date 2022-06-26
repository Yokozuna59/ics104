##
# This program reads user input asking for month, then prints the number of days in that month.
#

# Ask user to enter the month
userMonth = int(input("Enter a month: "))

# Check userMonth range
if (1 <= userMonth <= 12):
    if ((userMonth == 1) or (userMonth == 3) or (userMonth == 5) or (userMonth == 7) or (userMonth == 8) or (userMonth == 10) or (userMonth == 12)):
        output = "31 days"
    elif (userMonth == 4 or userMonth == 6 or userMonth == 9 or userMonth == 11):
        output = "30 days"
    else:
        output = "28 or 29 days"
else:
    output = "Wrong month"

# Print the result
print(output)