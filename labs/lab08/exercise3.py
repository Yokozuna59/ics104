##
# This program ask user to enter a secure password and ask him to enter it again if it's secure.
#

# Create fucntion checks if password has valid length
def isValidLength(password):
    return len(password) >= 8

# Create function checks if password has valid case
def isValidCase(password):
    containsLowerCase = False
    containsUpperCase = False

    for letter in password:
        if (letter.isupper()):
            containsUpperCase = True
        elif (letter.islower()):
            containsLowerCase = True

        if (containsLowerCase and containsUpperCase):
            return True
    return False

# Create function checks if password contains integer
def isContainNumber(password):
    for letter in password:
        if (letter.isdigit()):
            return True
    return False

# Create main fuction were the code starts
def main():
    correct_answer = False
    while not correct_answer:
        # Ask user for password
        firstPassword = input("Enter the password: ")

        if (isValidLength(firstPassword)) and (isValidCase(firstPassword)) and (isContainNumber(firstPassword)):
            secondPassword = input("Re-enter the password: ")

            if (firstPassword == secondPassword):
                print("The password is secure")
                correct_answer = True
            else:
                print("The two passwords don't match")
        else:
            print("Not a secure password")

# Execute the main function
if __name__ == "__main__":
    main()