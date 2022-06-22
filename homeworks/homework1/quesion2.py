##
# This program reads the user input of month index and prints.
#

# Define a long string contains all months
MONTHS = "%-9s %-9s %-9s %-9s %-9s %-9s %-9s %-9s %-9s %-9s %-9s %-9s" %("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Ask user to enter index month as the calendar
userMonth = int(input("Please enter an integer number representing a month (between 1 and 12): "))

# Get month index as its starts with 0
monthIndex = userMonth - 1

# Get month first letter index
monthFirstLetter = monthIndex*10

# Get month last letter index
monthLastLetter = monthIndex*10 + 8

# Get monthCompine each letter of month together
month = MONTHS[monthFirstLetter:monthLastLetter]

# Strip the month from empty spaces
monthWithNoSpace = month.strip()

# Print the month
print("Your month is %s." %monthWithNoSpace)