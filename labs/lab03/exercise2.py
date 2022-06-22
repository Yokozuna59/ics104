##
# This program generates a password using the user's inputs: first name and year of birth.
#

# Ask the user to enter his/her name and year of birth.
userFirstNameUpper = input("Enter student's first name: ").upper()
userBirthYear = int(input("Enter student's year of birth: "))

# Get the lowercase version of the first name
lowerFirstName = userFirstNameUpper.lower()

# Get the fist and last letter of the name
firstAndLastLetterOfName = userFirstNameUpper[0] + userFirstNameUpper[-1]

# Get the double of the year of birth
yearDouble = str(userBirthYear * 2)

print("Password = %s%s$%d" %(lowerFirstName, firstAndLastLetterOfName, yearDouble))