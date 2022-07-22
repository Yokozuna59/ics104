##
# This program prints the numeric value of user input grades.
#

# Create a dictionary grades with numeric value
grades = {"A+": 4.0, "A": 3.75, "B+": 3.5, "B": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0}

# Ask user for a grade
userGrade = input("Enter a grade: ")

# Print result
if (userGrade in grades):
    print("The numeric value of %s is %s" %(userGrade, grades[userGrade.upper()]))
else:
    print("Invalid grade")