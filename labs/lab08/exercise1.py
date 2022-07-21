##
# This program reverse user input.
#

# Create reverse function returns the reversed string
def reverse(string):
    return string[::-1]

# Create main fuction where the code starts
def main():
    # Ask user for input
    userInput = input("Enter a string: ")

    # Print the result
    print("The reversed of", userInput, "is", reverse(userInput))

# Execute the main function
if __name__ == "__main__":
    main()