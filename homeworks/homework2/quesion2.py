##
# This program prints every substring of user input in order of length.
#

# Create a function print every substring of a string in order of length
def printSubstring(string):
    string_length = len(string)
    for current_length in range(1, string_length+1):
        for i in range(string_length - current_length+1):
            print(string[i:i+current_length])

finished = False
while not finished:
    # ask for input
    userInput = input("Enter a string or an empty string to terminate the program: ")

    if (userInput == ""):
        print("Done...")
        finished = True
    else:
        printSubstring(userInput)