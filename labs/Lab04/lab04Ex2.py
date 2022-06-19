##
# This program read the user letter grade and print the weight of it.
#

# Ask the user to enter a grade
userLetterGrade = input("Enter a letter grade: ").upper()

# Check what user has entered
if (userLetterGrade == "A+"):
    gradeWeight = 4.0
elif (userLetterGrade == "A"):
    gradeWeight = 3.75
elif (userLetterGrade == "B+"):
    gradeWeight = 3.5
elif (userLetterGrade == "B"):
    gradeWeight = 3.0
elif (userLetterGrade == "C+"):
    gradeWeight = 2.5
elif (userLetterGrade == "C"):
    gradeWeight = 2.0
elif (userLetterGrade == "D+"):
    gradeWeight = 1.5
elif (userLetterGrade == "D"):
    gradeWeight = 1.0
elif (userLetterGrade == "F"):
    gradeWeight = 0.0
else:
    gradeWeight = -1

# Print the result
if (gradeWeight != -1):
    print("The numeric value is %.1f" %gradeWeight)
else:
    print("Invalid letter grade")