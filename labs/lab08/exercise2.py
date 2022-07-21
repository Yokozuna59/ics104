##
# This program check if user input is a leap year or not.
#

# Create isLeapYear function
def isLeapYear(year):
    if (year % 400 == 0):
        result = True
    elif (year % 4 == 0):
        result = True
    else:
        result = False
    return result

# Create main fuction were the code starts
def main():
    # Ask user for input
    yearInput = int(input("Enter a year: "))

    # Check if year is leap
    if (isLeapYear(yearInput)):
        result = "is a leap year"
    else:
        result = "is not a leap year"

    # Print the result
    print("Year", yearInput, result)

# Execute the main function
if __name__ == "__main__":
    main()